#Author - Deep Gupta
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

MYDATA = [
            [ "S.NO." , "DATE OF PURCHASING" , "NAME OF COURSE" , "SUBSCRIPTION TIME" , "PRICE OF COURSE(RS.)"],
            ["01" , "01/05/2024" , "PYTHON PROGRAMMING" , "LIFETIME" , "2,000"],
            ["02" , "05/05/2024" , "FULL STACK DEVELOPMENT" , "1 YEAR" , "5,000"],
            ["SUBTOTAL" , "" , "" , "" , "7,000"],
            ["DISCOUNT" , "" , "" , "" , "700"],
            ["TOTAL" , "" , "" , "" , "6,300"],
]

pdf = SimpleDocTemplate( "reciept.pdf" , papersize = A4)

styles = getSampleStyleSheet()

title_style = styles[ "Heading1" ]

title_style.alignment = 1

title = Paragraph( "Internshalla" , title_style )

style = TableStyle(
    [
        ( "BOX" , ( 0, 0), (-1,-1), 1 , colors.black),  
        ( "GRID" , ( 0, 0), (4,4), 1 , colors.black),
        ( "BACKGROUND" , ( 0, 0), (3,0), colors.green),
        ( "TEXTCOLOR" , ( 0, 0), (-1,0), colors.black),
        ( "ALIGN" , ( 0, 0), (-1,-1), "CENTER" , "BOLD"),
        ( "BACKGROUND" , ( 0, 1), (-1,-1), colors.palegreen)
    ]
)

table = Table( MYDATA , style = style )

pdf.build([ title , table])