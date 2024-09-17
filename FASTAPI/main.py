from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.api_integration import (
    ClassRPCSaleOrder, ClassRPCPurchaseOrder, ClassRPCEmployee, 
    ClassRPCProject, ClassRPCMRPProduction, ClassRPCStockQuant, 
    ClassRPCAssets, ClassRPCDashboard, ClassRPCQrCode
)
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Initialize Odoo clients
sale_order_client = ClassRPCSaleOrder(
    url='http://localhost:8069',
    db='DatabaseBaru',
    username='admin',
    password='admin'
)

purchase_order_client = ClassRPCPurchaseOrder(
    url='http://localhost:8069',
    db='DatabaseBaru',
    username='admin',
    password='admin'
)

employee_client = ClassRPCEmployee(
    url='http://localhost:8069',
    db='DatabaseBaru',
    username='admin',
    password='admin'
)

project_client = ClassRPCProject(
    url='http://localhost:8069',
    db='DatabaseBaru',
    username='admin',
    password='admin'
)

mrp_production_client = ClassRPCMRPProduction(
    url='http://localhost:8069',
    db='DatabaseBaru',
    username='admin',
    password='admin'
)

stock_quant_client = ClassRPCStockQuant(
    url='http://localhost:8069',
    db='DatabaseBaru',
    username='admin',
    password='admin'
)

assets_client = ClassRPCAssets(
    url='http://localhost:8069',
    db='DatabaseBaru',
    username='admin',
    password='admin'
)

dashboard_client = ClassRPCDashboard(
    url='http://localhost:8069',
    db='DatabaseBaru',
    username='admin',
    password='admin'
)

qr_code_client = ClassRPCQrCode(
    url='http://localhost:8069',
    db='DatabaseBaru',
    username='admin',
    password='admin'
)


# Pydantic Models
class SaleOrderSchema(BaseModel):
    partner_id: int
    date_order: str
    state: str


class PurchaseOrderSchema(BaseModel):
    partner_id: int
    date_order: str
    state: str


class EmployeeSchema(BaseModel):
    name: str
    email: str


class ProjectSchema(BaseModel):
    name: str
    user_id: int


class MRPProductionSchema(BaseModel):
    product_id: int
    product_qty: float
    state: str


class StockQuantSchema(BaseModel):
    product_id: int
    location_id: int
    quantity: float


class AssetSchema(BaseModel):
    name: str
    value: float
    asset_type: str


class DashboardSchema(BaseModel):
    name: str
    data: dict


class QRCodeSchema(BaseModel):
    name: str
    code: str


# CRUD Routes for Sale Order
@app.post("/sale_orders/")
def create_sale_order(sale_order: SaleOrderSchema):
    result = sale_order_client.create_sale_order(**sale_order.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Sale order creation failed")
    return {"message": "Sale order created", "result": result}


@app.get("/sale_orders/{sale_order_id}")
def read_sale_order(sale_order_id: int):
    result = sale_order_client.read_sale_order(sale_order_id)
    if not result:
        raise HTTPException(status_code=404, detail="Sale order not found")
    return result


@app.put("/sale_orders/{sale_order_id}")
def update_sale_order(sale_order_id: int, sale_order: SaleOrderSchema):
    result = sale_order_client.update_sale_order(sale_order_id, sale_order.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Sale order update failed")
    return {"message": "Sale order updated", "result": result}


@app.delete("/sale_orders/{sale_order_id}")
def delete_sale_order(sale_order_id: int):
    result = sale_order_client.delete_sale_order(sale_order_id)
    if not result:
        raise HTTPException(status_code=500, detail="Sale order deletion failed")
    return {"message": "Sale order deleted"}


# CRUD Routes for Purchase Order
@app.post("/purchase_orders/")
def create_purchase_order(purchase_order: PurchaseOrderSchema):
    result = purchase_order_client.create_purchase_order(**purchase_order.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Purchase order creation failed")
    return {"message": "Purchase order created", "result": result}


@app.get("/purchase_orders/{purchase_order_id}")
def read_purchase_order(purchase_order_id: int):
    result = purchase_order_client.read_purchase_order(purchase_order_id)
    if not result:
        raise HTTPException(status_code=404, detail="Purchase order not found")
    return result


@app.put("/purchase_orders/{purchase_order_id}")
def update_purchase_order(purchase_order_id: int, purchase_order: PurchaseOrderSchema):
    result = purchase_order_client.update_purchase_order(purchase_order_id, purchase_order.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Purchase order update failed")
    return {"message": "Purchase order updated", "result": result}


@app.delete("/purchase_orders/{purchase_order_id}")
def delete_purchase_order(purchase_order_id: int):
    result = purchase_order_client.delete_purchase_order(purchase_order_id)
    if not result:
        raise HTTPException(status_code=500, detail="Purchase order deletion failed")
    return {"message": "Purchase order deleted"}


# CRUD Routes for Employee
@app.post("/employees/")
def create_employee(employee: EmployeeSchema):
    result = employee_client.create_employee(**employee.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Employee creation failed")
    return {"message": "Employee created", "result": result}


@app.get("/employees/{employee_id}")
def read_employee(employee_id: int):
    result = employee_client.read_employee(employee_id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeSchema):
    result = employee_client.update_employee(employee_id, employee.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Employee update failed")
    return {"message": "Employee updated", "result": result}


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    result = employee_client.delete_employee(employee_id)
    if not result:
        raise HTTPException(status_code=500, detail="Employee deletion failed")
    return {"message": "Employee deleted"}


# CRUD Routes for Project
@app.post("/projects/")
def create_project(project: ProjectSchema):
    result = project_client.create_project(**project.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Project creation failed")
    return {"message": "Project created", "result": result}


@app.get("/projects/{project_id}")
def read_project(project_id: int):
    result = project_client.read_project(project_id)
    if not result:
        raise HTTPException(status_code=404, detail="Project not found")
    return result


@app.put("/projects/{project_id}")
def update_project(project_id: int, project: ProjectSchema):
    result = project_client.update_project(project_id, project.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Project update failed")
    return {"message": "Project updated", "result": result}


@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    result = project_client.delete_project(project_id)
    if not result:
        raise HTTPException(status_code=500, detail="Project deletion failed")
    return {"message": "Project deleted"}


# CRUD Routes for MRP Production
@app.post("/mrp_productions/")
def create_mrp_production(mrp_production: MRPProductionSchema):
    result = mrp_production_client.create_mrp_production(**mrp_production.dict())
    if not result:
        raise HTTPException(status_code=500, detail="MRP production creation failed")
    return {"message": "MRP production created", "result": result}


@app.get("/mrp_productions/{mrp_production_id}")
def read_mrp_production(mrp_production_id: int):
    result = mrp_production_client.read_mrp_production(mrp_production_id)
    if not result:
        raise HTTPException(status_code=404, detail="MRP production not found")
    return result


@app.put("/mrp_productions/{mrp_production_id}")
def update_mrp_production(mrp_production_id: int, mrp_production: MRPProductionSchema):
    result = mrp_production_client.update_mrp_production(mrp_production_id, mrp_production.dict())
    if not result:
        raise HTTPException(status_code=500, detail="MRP production update failed")
    return {"message": "MRP production updated", "result": result}


@app.delete("/mrp_productions/{mrp_production_id}")
def delete_mrp_production(mrp_production_id: int):
    result = mrp_production_client.delete_mrp_production(mrp_production_id)
    if not result:
        raise HTTPException(status_code=500, detail="MRP production deletion failed")
    return {"message": "MRP production deleted"}


# CRUD Routes for Stock Quant
@app.post("/stock_quants/")
def create_stock_quant(stock_quant: StockQuantSchema):
    result = stock_quant_client.create_stock_quant(**stock_quant.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Stock quant creation failed")
    return {"message": "Stock quant created", "result": result}


@app.get("/stock_quants/{stock_quant_id}")
def read_stock_quant(stock_quant_id: int):
    result = stock_quant_client.read_stock_quant(stock_quant_id)
    if not result:
        raise HTTPException(status_code=404, detail="Stock quant not found")
    return result


@app.put("/stock_quants/{stock_quant_id}")
def update_stock_quant(stock_quant_id: int, stock_quant: StockQuantSchema):
    result = stock_quant_client.update_stock_quant(stock_quant_id, stock_quant.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Stock quant update failed")
    return {"message": "Stock quant updated", "result": result}


@app.delete("/stock_quants/{stock_quant_id}")
def delete_stock_quant(stock_quant_id: int):
    result = stock_quant_client.delete_stock_quant(stock_quant_id)
    if not result:
        raise HTTPException(status_code=500, detail="Stock quant deletion failed")
    return {"message": "Stock quant deleted"}


# CRUD Routes for Assets
@app.post("/assets/")
def create_asset(asset: AssetSchema):
    result = assets_client.create_asset(**asset.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Asset creation failed")
    return {"message": "Asset created", "result": result}


@app.get("/assets/{asset_id}")
def read_asset(asset_id: int):
    result = assets_client.read_asset(asset_id)
    if not result:
        raise HTTPException(status_code=404, detail="Asset not found")
    return result


@app.put("/assets/{asset_id}")
def update_asset(asset_id: int, asset: AssetSchema):
    result = assets_client.update_asset(asset_id, asset.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Asset update failed")
    return {"message": "Asset updated", "result": result}


@app.delete("/assets/{asset_id}")
def delete_asset(asset_id: int):
    result = assets_client.delete_asset(asset_id)
    if not result:
        raise HTTPException(status_code=500, detail="Asset deletion failed")
    return {"message": "Asset deleted"}


# CRUD Routes for Dashboard
@app.post("/dashboards/")
def create_dashboard(dashboard: DashboardSchema):
    result = dashboard_client.create_dashboard(**dashboard.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Dashboard creation failed")
    return {"message": "Dashboard created", "result": result}


@app.get("/dashboards/{dashboard_id}")
def read_dashboard(dashboard_id: int):
    result = dashboard_client.read_dashboard(dashboard_id)
    if not result:
        raise HTTPException(status_code=404, detail="Dashboard not found")
    return result


@app.put("/dashboards/{dashboard_id}")
def update_dashboard(dashboard_id: int, dashboard: DashboardSchema):
    result = dashboard_client.update_dashboard(dashboard_id, dashboard.dict())
    if not result:
        raise HTTPException(status_code=500, detail="Dashboard update failed")
    return {"message": "Dashboard updated", "result": result}


@app.delete("/dashboards/{dashboard_id}")
def delete_dashboard(dashboard_id: int):
    result = dashboard_client.delete_dashboard(dashboard_id)
    if not result:
        raise HTTPException(status_code=500, detail="Dashboard deletion failed")
    return {"message": "Dashboard deleted"}


# CRUD Routes for QR Code
@app.post("/qrcodes/")
def create_qr_code(qr_code: QRCodeSchema):
    result = qr_code_client.create_qr_code(**qr_code.dict())
    if not result:
        raise HTTPException(status_code=500, detail="QR code creation failed")
    return {"message": "QR code created", "result": result}


@app.get("/qrcodes/{qr_code_id}")
def read_qr_code(qr_code_id: int):
    result = qr_code_client.read_qr_code(qr_code_id)
    if not result:
        raise HTTPException(status_code=404, detail="QR code not found")
    return result


@app.put("/qrcodes/{qr_code_id}")
def update_qr_code(qr_code_id: int, qr_code: QRCodeSchema):
    result = qr_code_client.update_qr_code(qr_code_id, qr_code.dict())
    if not result:
        raise HTTPException(status_code=500, detail="QR code update failed")
    return {"message": "QR code updated", "result": result}


@app.delete("/qrcodes/{qr_code_id}")
def delete_qr_code(qr_code_id: int):
    result = qr_code_client.delete_qr_code(qr_code_id)
    if not result:
        raise HTTPException(status_code=500, detail="QR code deletion failed")
    return {"message": "QR code deleted"}
