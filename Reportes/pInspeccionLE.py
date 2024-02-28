from fpdf import FPDF
from datetime import date
import locale

from django.http import FileResponse
from InspeccionLoteApp.models import *
from PresupuestoVApp.models import *


class pinspl(FPDF):
    
    def pInspeccionLE(request, id ):
        try:
            pil=PrimeraInspLot.objects.get(Id=id)
        except PrimeraInspLot.DoesNotExist:
            pil=""
        try:
            inspeccionl=InspeccionLote.objects.get(Id=pil.IdInspeccionLote.Id)
        except InspeccionLote.DoesNotExist:
            inspeccionl=""
        try:
            pdg= PresupuestoViviDatGen.objects.get(IdSolicitud=inspeccionl.IdSolicitud.Id)
        except PresupuestoViviDatGen.DoesNotExist:
            pdg= ""
        try:
            do= DatosObra.objects.get(IdSolicitud=inspeccionl.IdSolicitud.Id)
        except DatosObra.DoesNotExist:
            do=""       
        try:
            DPipl = DescripcionProyInsLot.objects.get(IdInspeccionLote=inspeccionl.Id)
        except DescripcionProyInsLot.DoesNotExist:
            DPipl=""


        pdf=FPDF(orientation='P', unit='mm', format='Letter')
        pdf.add_page()
        #pdf.multi_cell(w=0, h=40, txt='', border=1)
        #Margenes de la pagina
        pdf.set_auto_page_break(auto=True, margin=5)
        pdf.set_draw_color(0,0,0)
        pdf.set_line_width(0.5)
        pdf.rect(5, 3,205,260)
     
        pdf.rect(6, 4,203,50)
        pdf.set_line_width(0.1)

        pdf.rect(10, 58,196,167)
        pdf.set_line_width(0.1)

        try:  
            # Agregar la imagen desde la instancia pil
            img_path = pil.Esquema.path  # Asumiendo pil.esquema que es un campo FileField o ImageField
            x = 11  # Coordenada horizontal 
            y = 75  # Coordenada vertical... arriba
            w = 194 # Ancho de la imagen en puntos
            h = 147  # Altura de la imagen en puntos
            pdf.image(img_path , x=x, y=y, w=w, h=h)
        except:
            pass

        pdf.image('TesisApp\static\TesisApp\images\logohabib.png', x=7, y=6, w=43, h=28)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=45,h=8,txt='', border=0, align='C', fill=False)
        pdf.cell(w=0,h=8,txt='ESQUEMA DE UBICACIÓN DEL INMUEBLE', border=1,  align='C', fill=False, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=45,h=5,txt='', border=0, align='C', fill=False)
        pdf.cell(w=40,h=5,txt='AGENCIA:', border=1,  align='L', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt=inspeccionl.IdSolicitud.IdPerfil.IdAgencia.Nombre if hasattr(inspeccionl, 'IdSolicitud') else '', border=1,  align='L', fill=False, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=45,h=5,txt='', border=0, align='C', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=40,h=5,txt='FECHA:', border=1,  align='L', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt=str(pil.Fecha) if hasattr(pil, 'Fecha') else '', border=1,  align='L', fill=False, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=45,h=5,txt='', border=0, align='C', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=65,h=5,txt='TIEMPO DE CONSTRUCCIÓN:', border=0,  align='L', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt=pdg.TiempoCons if hasattr(pdg, 'TiempoCons') else '', border=0,  align='C', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=40,h=5,txt='CLIENTE:', border=1, align='L', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt=(inspeccionl.IdSolicitud.IdPerfil.Nombres if hasattr(inspeccionl, 'IdSolicitud') else '') +' '+ (inspeccionl.IdSolicitud.IdPerfil.Apellidos if hasattr(inspeccionl, 'IdSolicitud') else '' ), border=1,  align='L', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=65,h=6,txt='MODELO DE LA VIVIENDA:', border=1, align='C', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=35,h=6,txt=DPipl.ModeloViviCon if hasattr(DPipl, 'ModeloViviCon') else '', border=1,  align='L', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=40,h=6,txt='MUNICIPIO:', border=1, align='C', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=6,txt=inspeccionl.IdSolicitud.IdPerfil.municipio.distri if hasattr(inspeccionl, 'IdSolicitud') else '', border=1,  align='L', fill=False, ln=1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=65,h=6,txt='DIRECCIÓN DE LA MEJORA:', border=1, align='C', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=50,h=6,txt=do.DireccionExac if hasattr(do, 'DireccionExac') else '', border=1,  align='L', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=40,h=6,txt='TELEFONO:', border=1, align='C', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=6,txt=inspeccionl.IdSolicitud.IdPerfil.telefono if hasattr(inspeccionl, 'IdSolicitud') else '', border=1,  align='L', fill=False, ln=1)
        pdf.cell(w=0,h=5,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=120,h=6,txt='', border='LRT', align='C', fill=False)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=38,h=6,txt=str(inspeccionl.Latitud) if hasattr(inspeccionl, 'Latitud') else '', border=1,  align='L', fill=False)
        pdf.cell(w=38,h=6,txt=str(inspeccionl.Longitud) if hasattr(inspeccionl, 'Longitud') else '', border=1,  align='L', fill=False, ln=1)      
        pdf.cell(w=120,h=6,txt='', border='LR', align='C', fill=False)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w=38,h=6,txt='LATITUD', border=1,  align='L', fill=False)
        pdf.cell(w=38,h=6,txt='LONGITUD', border=1,  align='L', fill=False, ln=1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w=0,h=5,txt='', border=0,  align='C', fill=False, ln=1)
        pdf.cell(w=0,h=150,txt='', border=0,  align='C', fill=False, ln=1)
        pdf.cell(w=0,h=1,txt='', border='',  align='C', fill=False, ln=1)
        pdf.cell(w=95,h=32,txt='', border=1, align='C', fill=False)
        pdf.cell(w=3,h=32,txt='', border=0, align='C', fill=False)
        pdf.cell(w=65,h=32,txt='', border=1, align='C', fill=False)
        pdf.cell(w=2,h=32,txt='', border=0, align='C', fill=False)
        pdf.cell(w=30,h=32,txt='', border=1, align='C', fill=False)

        pdf.text(x=109, y=234, txt='SELLO ')
        pdf.text(x=15, y=239, txt='F. ')
        pdf.line(15, 240, 90, 240)
        pdf.text(x=15, y=245, txt='TECNICO EN SERVICIOS CONSTRUCTIVOS ')
        
        

        pdf.output('pInspeccionlEsq.pdf', 'F')
        return FileResponse(open('pInspeccionlEsq.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
