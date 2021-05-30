from arrow import utcnow
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,Image
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import black, white
from reportlab.pdfgen import canvas


# ======================= CLASE PDF =========================

class PDF(object):
    #Exportar una lista de diccionarios a una tabla en un
    #archivo PDF.
    
    def __init__(self, nombrePDF,formulacion,soluciones):
        super(PDF, self).__init__()

        self.nombrePDF = nombrePDF

        self.formulacion=formulacion
        self.soluciones=soluciones

        self.estilos = getSampleStyleSheet()

    @staticmethod
    def _encabezadoPiePagina(canvas, archivoPDF):
        #Guarde el estado de nuestro lienzo para que podamos aprovecharlo
        
        canvas.saveState()
        estilos = getSampleStyleSheet()

        alineacion = ParagraphStyle(name="alineacion", alignment=TA_RIGHT,
                                    parent=estilos["Normal"])
 
        # Encabezado
        encabezadoNombre = Paragraph("Asignación caso Mochila", estilos["Normal"])
        anchura, altura = encabezadoNombre.wrap(archivoPDF.width, archivoPDF.topMargin)
        encabezadoNombre.drawOn(canvas, archivoPDF.leftMargin, 736)

        fecha = utcnow().to("local").format("dddd, DD - MMMM - YYYY", locale="es")
        fechaReporte = fecha.replace("-", "de")

        encabezadoFecha = Paragraph(fechaReporte, alineacion)
        anchura, altura = encabezadoFecha.wrap(archivoPDF.width, archivoPDF.topMargin)
        encabezadoFecha.drawOn(canvas, archivoPDF.leftMargin, 736)
 
        # Pie de página
        piePagina = Paragraph("Grupo 1", estilos["Normal"])
        anchura, altura = piePagina.wrap(archivoPDF.width, archivoPDF.bottomMargin)
        piePagina.drawOn(canvas, archivoPDF.leftMargin, 15 * mm + (0.2 * inch))
 
        # Suelta el lienzo
        canvas.restoreState()

    def convertirDatos(self,cabecera,datos):
        #Convertir la lista de diccionarios a una lista de listas para crear
        #la tabla PDF.

        estiloEncabezado = ParagraphStyle(name="estiloEncabezado", alignment=TA_LEFT,
                                          fontSize=10, textColor=white,
                                          fontName="Helvetica-Bold",
                                          parent=self.estilos["Normal"])

        estiloNormal = self.estilos["Normal"]
        estiloNormal.alignment = TA_LEFT

        claves, nombres = zip(*[[k, n] for k, n in cabecera])

        encabezado = [Paragraph(nombre, estiloEncabezado) for nombre in nombres]
        nuevosDatos = [tuple(encabezado)]

        for dato in datos:
            nuevosDatos.append([Paragraph(str(dato[clave]), estiloNormal) for clave in claves])
            
        return nuevosDatos
        
    def Exportar(self):
        #Exportar los datos a un archivo PDF.

        alineacionTitulo = ParagraphStyle(name="centrar", alignment=TA_CENTER, fontSize=13,
                                          leading=10, textColor=black,
                                          parent=self.estilos["Heading1"])

        alineaciontexto = ParagraphStyle(name="estilotexto", alignment=TA_LEFT, fontSize=11,
                                          leading=10, textColor=black,
                                          parent=self.estilos["Normal"])
        
        self.ancho, self.alto = letter

        historia = []
        #========================== Tabla de datos del problema =======================================
        cabeceraformuulacion = (
        ("des", "Descripción"),
        ("peso", "Peso"),
        ("bene", "Beneficio"),
        )
        datosformulacion=[]
        for dato in self.formulacion[1:]:
            datosformulacion.append({"des":dato[0] , "peso": dato[1], "bene": dato[2]})

        convertirDatos = self.convertirDatos(cabeceraformuulacion,datosformulacion)
    
        tabla = Table(convertirDatos, colWidths=(self.ancho-100)/len(cabeceraformuulacion), hAlign="CENTER")
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0),(-1, 0), black),
            ("ALIGN", (0, 0),(0, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), # Texto centrado y alineado a la izquierda
            ("INNERGRID", (0, 0), (-1, -1), 0.50, black), # Lineas internas
            ("BOX", (0, 0), (-1, -1), 0.25, black), # Linea (Marco) externa
            ]))
        #===========================================================================================
        historia.append(Spacer(1, 0.30 * inch))
        I = Image('mochila.png',189,189)
       
        historia.append(I)

        historia.append(Spacer(1, 0.30 * inch))
        historia.append(Paragraph("Formulación del Problema", alineacionTitulo))
        historia.append(Paragraph("Capacidad: "+ str(self.formulacion[0]), alineaciontexto))
        historia.append(Spacer(1, 0.16 * inch))
        historia.append(tabla)
        historia.append(Spacer(1, 0.30 * inch))

        #========================== Tablas de datos de la Solucion =======================================
        cabeceraSolucion = (
        ("des", "Descripción"),
        ("canti", "Cantidad"),
        ("peso", "Peso"),
        ("uti", "Utilidad"),
        )
        datosSolucion=[]
        
        historia.append(Paragraph("Solución del Problema", alineacionTitulo))
        for i in range(len(self.soluciones)):
            historia.append(Paragraph("Solución "+ str(i+1), alineaciontexto))
            historia.append(Spacer(1, 0.16 * inch))
            for dato in self.soluciones[i]:
                datosSolucion.append({"des":dato[0] ,"canti":dato[1], "peso": dato[2], "uti": dato[3]})

            convertirDatos = self.convertirDatos(cabeceraSolucion,datosSolucion)
            tabla = Table(convertirDatos, colWidths=(self.ancho-100)/len(cabeceraSolucion), hAlign="CENTER")
            tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0),(-1, 0), black),
            ("ALIGN", (0, 0),(0, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), # Texto centrado y alineado a la izquierda
            ("INNERGRID", (0, 0), (-1, -1), 0.50, black), # Lineas internas
            ("BOX", (0, 0), (-1, -1), 0.25, black), # Linea (Marco) externa
            ]))
            historia.append(tabla)
        #===========================================================================================

        archivoPDF = SimpleDocTemplate(self.nombrePDF, leftMargin=50, rightMargin=50, pagesize=letter,
                                       title="solucion mochila", author="Edwin Diaz")
        
        try:
            archivoPDF.build(historia, onFirstPage=self._encabezadoPiePagina,
                             onLaterPages=self._encabezadoPiePagina,
                             canvasmaker=numeracionPaginas)
            
         # +------------------------------------+
            return "PDF generado con éxito."
         # +------------------------------------+
        except PermissionError:
         # +--------------------------------------------+  
            return "Error inesperado: Permiso denegado."
         # +--------------------------------------------+


# ================== CLASE numeracionPaginas =======================

class numeracionPaginas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        #Agregar información de la página a cada página (página x de y)
        numeroPaginas = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(numeroPaginas)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)
 
    def draw_page_number(self, conteoPaginas):
        self.drawRightString(204 * mm, 15 * mm + (0.2 * inch),
                             "Página {} de {}".format(self._pageNumber, conteoPaginas))        


# ===================== Funcion generar tablas =====================

def generarPDF(nombrePDF,datos_problema,soluciones):
    #llamar la función Exportar, la cuál esta en la clase reportePDF, a esta clase le pasamos el título de la tabla, la
    #cabecera y los datos que llevará.
    pdf = PDF (nombrePDF,datos_problema,soluciones).Exportar()
    print(pdf)
