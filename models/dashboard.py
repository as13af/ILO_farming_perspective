from odoo import models, fields, api
import json

class ILODashboard(models.Model):
    _name = 'ilo.dashboard'
    _description = 'Custom Dashboard for ILO Programs'

    name = fields.Char(string='Name', required=True)
    # Assets Data
    assets_data = fields.One2many('ilo.assets', 'dashboard_id', string='Assets Data')
    total_area_usage = fields.Float(string='Total Area Usage', compute='_compute_total_area_usage', store=True)

    # Process Percentages
    process_percentage = fields.Float(string='Process Percentage', compute='_compute_status_percentages', store=True)
    completed_percentage = fields.Float(string='Completed Percentage', compute='_compute_status_percentages', store=True)

    # MRP Production Data
    mrp_production_data = fields.One2many('mrp.production', 'dashboard_id', string='MRP Productions')
    mrp_process_percentage = fields.Float(string='Process Percentage', compute='_compute_mrp_status_percentages', store=True)
    mrp_completed_percentage = fields.Float(string='Completed Percentage', compute='_compute_mrp_status_percentages', store=True)
    regional_production_data = fields.Text(string='Regional Production Data', compute='_compute_regional_production_data', store=True)

    # Computing Total Area Usage
    @api.depends('assets_data.area_ha')
    def _compute_total_area_usage(self):
        for record in self:
            record.total_area_usage = sum(asset.area_ha for asset in record.assets_data)

    # Computing Status Percentages
    @api.depends('assets_data.planting_status')
    def _compute_status_percentages(self):
        for record in self:
            total_assets = len(record.assets_data)
            process_count = len(record.assets_data.filtered(lambda asset: asset.planting_status == 'proses'))
            completed_count = len(record.assets_data.filtered(lambda asset: asset.planting_status == 'selesai'))

            record.process_percentage = (process_count / total_assets) * 100 if total_assets else 0
            record.completed_percentage = (completed_count / total_assets) * 100 if total_assets else 0

    # Computing MRP Status Percentages
    @api.depends('mrp_production_data.quality_check_status')
    def _compute_mrp_status_percentages(self):
        for record in self:
            total_productions = len(record.mrp_production_data)
            process_count = len(record.mrp_production_data.filtered(lambda prod: prod.quality_check_status == 'pending'))
            completed_count = len(record.mrp_production_data.filtered(lambda prod: prod.quality_check_status == 'passed'))

            record.mrp_process_percentage = (process_count / total_productions) * 100 if total_productions else 0
            record.mrp_completed_percentage = (completed_count / total_productions) * 100 if total_productions else 0

    # Computing Regional Production Data
    @api.depends('mrp_production_data.location_dest_id', 'mrp_production_data.state')
    def _compute_regional_production_data(self):
        for record in self:
            regional_data = {}
            for production in record.mrp_production_data:
                region = production.location_dest_id.name
                if region not in regional_data:
                    regional_data[region] = {'completed': 0, 'in_progress': 0}
                if production.state == 'done':
                    regional_data[region]['completed'] += 1
                else:
                    regional_data[region]['in_progress'] += 1
            record.regional_production_data = json.dumps(regional_data)
