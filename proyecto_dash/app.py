from fastapi import FastAPI, Request, staticfiles
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from mongoengine import *
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta
from bson.objectid import ObjectId


app = FastAPI()
app.mount("/static", staticfiles.StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



# Conexión a MongoDB
try:
    connect(
        db="registro_oac",
        username="heimdall",
        password="Nn77Tw0WPM8Az1W1",
        host="mongodb+srv://cluster0.3vudx.mongodb.net",
        authentication_source='admin',
        ssl=True,
    )
    print("Conexión a MongoDB exitosa")
except ConnectionFailure as e:
    print(f"No se pudo conectar a MongoDB: {e}")

# Modelo de datos con mongoengine
class datos_formulario(Document):
    nombre = StringField()
    correo = EmailField()
    cargo = StringField()
    numero_cedula = StringField()
    numero_telefono_jefe = StringField()
    estado = StringField()
    municipio = StringField()
    nombre_organismo = StringField()
    instancia = StringField()
    mes_reportado = StringField()
    nombre_llenado = StringField()
    correo_llenado = EmailField()
    cargo_llenado = StringField()
    numero_cedula_llenado = StringField()
    numero_telefono_llenado = StringField()
    cantidad_denuncias = IntField()
    cantidad_reclamos = IntField()
    cantidad_quejas = IntField()
    cantidad_peticiones = IntField()
    cantidad_sugerencias = IntField()
    cantidad_asesorias = IntField()
    cantidad_poblacion_masc = IntField()
    cantidad_poblacion_fem = IntField()
    cantidad_talleres_oipp = IntField()
    cantidad_charlas_oipp = IntField ()
    cantidad_conversatorios_oipp = IntField()
    cantidad_jornadas_oipp = IntField()
    cantidad_forochats_oipp = IntField()
    cantidad_adulto_masculino_atentido_oipp = IntField() 
    cantidad_adulto_femenino_atentida_oipp = IntField()
    nombre_escuela_se = StringField()
    cantidad_actividades_se = StringField()
    cantidad_talleres_se = IntField()
    cantidad_charlas_se = IntField()
    cantidad_conversatorios_se = IntField()
    cantidad_jornadas_se = IntField()
    cantidad_forochats_se = IntField()
    cantidad_ninosyadol_masculino_se = IntField()
    cantidad_ninasyadol_femenino_se = IntField()
    cantidad_adultos_masculino_atendidos_se = IntField()
    cantidad_adultos_femenino_atendidos_se = IntField()
    nombre_ministerio_ap = StringField()
    cantidad_actividades_ap = StringField()
    cantidad_talleres_ap = IntField()
    cantidad_charlas_ap = IntField()
    cantidad_jornadas_ap = IntField()
    cantidad_forochats_ap = IntField()
    cantidad_funcionarios_masculino_ap = IntField()
    cantidad_funcionarios_femenino_ap = IntField()
    observaciones = StringField()

    meta = {'collection': 'formulario'}

# Modelo Pydantic para la respuesta de la API
class DatoResponse(BaseModel):
    id: Optional[str] = None
    nombre: Optional[str] = None
    correo: Optional[str] = None
    cargo: Optional[str] = None
    cedula: Optional[str] = None
    telefono: Optional[str] = None
    estado: Optional[str] = None
    municipio: Optional[str] = None
    organismo: Optional[str] = None
    instancia : Optional[str] = None
    mes : Optional[str] = None
    nombre_llenado : Optional[str] = None
    correo_llenado : Optional[str] = None
    cargo_llenado : Optional[str] = None
    numero_cedula_llenado : Optional[str] = None
    numero_telefono_llenado : Optional[str] = None
    denuncias : Optional[int] = None
    reclamos : Optional[int] = None
    quejas : Optional[int] = None
    peticiones : Optional[int] = None
    sugerencias : Optional[int] = None
    asesorias : Optional[int] = None
    pob_masc : Optional[int] = None
    pob_fem : Optional[int] = None
    cantidad_talleres_oipp : Optional[int] = None
    cantidad_charlas_oipp : Optional[int] = None
    cantidad_conversatorios_oipp :Optional[int] = None
    cantidad_jornadas_oipp : Optional[int] = None
    cantidad_forochats_oipp : Optional[int] = None
    cantidad_adulmasc_atend_oipp : Optional[int] = None
    cantidad_adulfem_atend_oipp : Optional[int] = None
    nombre_escuela_se : Optional[str] = None
    cantidad_actividades_se : Optional[str] = None
    cantidad_talleres_se : Optional[int] = None
    cantidad_charlas_se : Optional[int] = None
    cantidad_conversatorios_se : Optional[int] = None
    cantidad_jornadas_se :Optional[int] = None
    cantidad_forochats_se :Optional[int] = None
    cantidad_ninos_masc_se :Optional[int] = None
    cantidad_ninos_femenino_se : Optional[int] = None
    cantidad_adulmasc_atend_se : Optional[int] = None
    cantidad_adulfem_atend_se : Optional[int] = None
    nombre_ministerio_ap : Optional[str] = None
    cantidad_actividades_ap : Optional[str] = None
    cantidad_talleres_ap : Optional[int] = None
    cantidad_charlas_ap : Optional[int] = None
    cantidad_jornadas_ap : Optional[int] = None
    cantidad_forochats_ap : Optional[int] = None
    cantidad_funcionarios_masculino_ap : Optional[int] = None
    cantidad_funcionarios_femenino_ap : Optional[int] = None
    observaciones : Optional[str] = None
   
    # ... (otros campos)


@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/logout")
async def logout():
    response = RedirectResponse(url="/", status_code=303)
    #response.delete_cookie("sessionid")
    return response

@app.get("/dashboard", response_class=HTMLResponse)
def read_root(request: Request):
    datos = datos_formulario.objects().order_by('-id').limit(100)
    print(f"Cantidad de datos recuperados: {len(datos)}") # Agrega esta línea
    hoy = datetime.now()
    inicio_dia = datetime(hoy.year, hoy.month, hoy.day)
    inicio_semana = hoy - timedelta(days=hoy.weekday())
    
    # Convertir fechas a ObjectId para comparación
    object_id_hoy = ObjectId.from_datetime(inicio_dia)
    object_id_semana = ObjectId.from_datetime(inicio_semana)
    
    registros_hoy = datos_formulario.objects(id__gte=object_id_hoy).count()
    registros_semana = datos_formulario.objects(id__gte=object_id_semana).count()
    total_registros = datos_formulario.objects.count()
    
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "datos": datos,
        "registros_hoy": registros_hoy,
        "registros_semana": registros_semana,
        "total_registros": total_registros
    })




@app.get("/api/datos", response_model=List[DatoResponse])
def get_datos():
    datos = datos_formulario.objects().limit(1000)
    return [DatoResponse(id=str(dato.id), **dato.to_mongo().to_dict()) for dato in datos]


@app.get("/api/datos/{id}", response_model=DatoResponse)
def get_dato(id: str):
    dato = datos_formulario.objects(id=id).first()
    data = dato.to_mongo().to_dict()
    return {
        "nombre" : dato.nombre,
        "correo" :  dato.correo, 
        "cargo" : dato.cargo, 
        "cedula" : dato.numero_cedula, 
        "telefono" :  dato.numero_telefono_jefe, 
        "estado" : dato.estado ,
        "municipio" : dato.municipio, 
        "organismo" : dato.nombre_organismo, 
        "instancia": dato.instancia ,
        "mes" : dato.mes_reportado ,
        "nombre_llenado":dato.nombre_llenado ,
        "cargo_llenado" : dato.cargo_llenado ,
        "numero_cedula_llenado" : dato.numero_cedula_llenado ,
        "numero_telefono_llenado" :dato.numero_telefono_llenado ,
        "correo_llenado" : dato.correo_llenado ,
        "denuncias" : dato.cantidad_denuncias ,
        "reclamos" : dato.cantidad_reclamos,
        "quejas" : dato.cantidad_quejas ,
        "peticiones" : dato.cantidad_peticiones ,
        "sugerencias" : dato.cantidad_sugerencias, 
        "asesorias" : dato.cantidad_asesorias ,
        "pob_masc" : dato.cantidad_poblacion_masc ,
        "pob_fem" : dato.cantidad_poblacion_fem ,
        "cantidad_talleres_oipp": dato.cantidad_talleres_oipp,
        "cantidad_charlas_oipp" : dato.cantidad_charlas_oipp ,
        "cantidad_conversatorios_oipp" : dato.cantidad_conversatorios_oipp,
        "cantidad_jornadas_oipp" : dato.cantidad_jornadas_oipp ,
        "cantidad_forochats_oipp" : dato.cantidad_forochats_oipp ,
        "cantidad_adulmasc_atend_oipp" :dato.cantidad_adulto_masculino_atentido_oipp ,
        "cantidad_adulfem_atend_oipp" :dato.cantidad_adulto_femenino_atentida_oipp ,
        "nombre_escuela_se" :dato.nombre_escuela_se ,
        "cantidad_actividades_se" :dato.cantidad_actividades_se ,
        "cantidad_talleres_se" :dato.cantidad_talleres_se ,
        "cantidad_charlas_se" :dato.cantidad_charlas_se,
        "cantidad_conversatorios_se" :dato.cantidad_conversatorios_se ,
        "cantidad_jornadas_se" :dato.cantidad_jornadas_se ,
        "cantidad_forochats_se": data.get("cantidad_forochats_se", 0),
        "cantidad_ninos_masc_se" :dato.cantidad_ninosyadol_masculino_se ,
        "cantidad_ninos_femenino_se" :dato.cantidad_ninasyadol_femenino_se ,
        "cantidad_adulmasc_atend_se" :dato.cantidad_adultos_masculino_atendidos_se ,
        "cantidad_adulfem_atend_se" :dato.cantidad_adultos_femenino_atendidos_se ,
        "nombre_ministerio_ap" :dato.nombre_ministerio_ap ,
        "cantidad_actividades_ap" :dato.cantidad_actividades_ap,
        "cantidad_talleres_ap" :dato.cantidad_talleres_ap ,
        "cantidad_charlas_ap" :dato.cantidad_charlas_ap ,
        "cantidad_jornadas_ap" :dato.cantidad_jornadas_ap ,
        "cantidad_forochats_ap" :dato.cantidad_forochats_ap ,
        "cantidad_funcionarios_masculino_ap" :dato.cantidad_funcionarios_masculino_ap ,
        "cantidad_funcionarios_femenino_ap" :dato.cantidad_funcionarios_femenino_ap ,
        "observaciones" :dato.observaciones
    }
    

@app.delete("/api/datos/{id}")
def delete_dato(id: str):
    try:
        # Eliminar el registro
        dato = datos_formulario.objects(id=id).first()
        if not dato:
            return JSONResponse(status_code=404, content={"message": "Registro no encontrado"})
        
        dato.delete()
        
        # Calcular los nuevos contadores
        hoy = datetime.now()
        inicio_dia = datetime(hoy.year, hoy.month, hoy.day)
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        
        object_id_hoy = ObjectId.from_datetime(inicio_dia)
        object_id_semana = ObjectId.from_datetime(inicio_semana)
        
        registros_hoy = datos_formulario.objects(id__gte=object_id_hoy).count()
        registros_semana = datos_formulario.objects(id__gte=object_id_semana).count()
        total_registros = datos_formulario.objects.count()
        
        return {
            "message": "Registro eliminado correctamente",
            "counters": {
                "hoy": registros_hoy,
                "semana": registros_semana,
                "total": total_registros
            }
        }
        
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error al eliminar: {str(e)}"})