from flask import render_template, request, session, redirect, url_for, Flask

host = "0.0.0.0"
port = 80
app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=["POST", "GET"])
@app.route('/index', methods=["POST", "GET"])
def index():
	if request.method == "POST":

		if "revBsueldo" in request.form:
			revBsueldo = request.form["revBsueldo"]
			try:
				revBsueldo = float(revBsueldo)
				if revBsueldo < 0:
					return render_template('index.html',ValueError='ValueError')
				sueldoliquido = calculaLiquido(revBsueldo)
				return render_template('index.html',sueldoliquido=sueldoliquido)
			except ValueError:
				return render_template('index.html',ValueError='ValueError')

		elif "revLsueldo" in request.form:
			revLsueldo = request.form["revLsueldo"]
			try:
				revLsueldo = float(revLsueldo)
				if revLsueldo < 0:
					return render_template('index.html',ValueError='ValueError')
				sueldobruto = calculaBruto(revLsueldo)
				return render_template('index.html',sueldobruto=sueldobruto)
			except ValueError:
				return render_template('index.html',ValueError='ValueError')

	return render_template('index.html')

def calculaLiquido(sueldo):
	SueldoBruto = sueldo

	afp = request.form["afp"]
	if afp == 'Capital' :
		afp = 12.97
	elif afp == 'Cuprum' :
		afp = 12.97
	elif afp == 'Habitat' :
		afp = 12.80
	elif afp == 'PlanVital' :
		afp = 12.69
	elif afp == 'ProVida' :
		afp = 12.98
	elif afp == 'Modelo' :
		afp = 12.30

	DescuentoSalud = SueldoBruto * (7/100)

	DescuentoPrevisional = SueldoBruto *( afp/100) 

	SeguroCesantia = SueldoBruto * (0.6/100)

	LiquidoImponible = SueldoBruto - (DescuentoSalud + DescuentoPrevisional + SeguroCesantia)

	Factor = ""
	CantidadRebajar = ""

	if LiquidoImponible>= 0 and LiquidoImponible <= 646920: 
		Factor = 0
		CantidadRebajar = 0

	elif LiquidoImponible>= 646921 and LiquidoImponible <= 1437600: 
		Factor = 0.04
		CantidadRebajar = 25876.80

	elif LiquidoImponible>= 1437600.01 and LiquidoImponible <= 2396000: 
		Factor = 0.08
		CantidadRebajar = 83380.80

	elif LiquidoImponible>= 2396000.01 and LiquidoImponible <= 3354400: 
		Factor = 0.135
		CantidadRebajar = 215160.80

	elif LiquidoImponible>= 3354400.01 and LiquidoImponible <= 4312800: 
		Factor = 0.23
		CantidadRebajar = 533828.80

	elif LiquidoImponible>= 4312800.01 and LiquidoImponible <= 5750400: 
		Factor = 0.304
		CantidadRebajar = 852976

	elif LiquidoImponible>= 5750400.01: 
		Factor = 0.35
		CantidadRebajar = 1117494.40


	ImpuestoRenta = (LiquidoImponible * Factor) - CantidadRebajar 


	SueldoLiquido = LiquidoImponible - ImpuestoRenta 



	return SueldoLiquido

def calculaBruto(sueldo):
	SueldoLiquido = sueldo
	Factor = ""
	CantidadRebajar = ""

	if SueldoLiquido <=646920.00: 
		Factor = 0
		CantidadRebajar = 0

	if SueldoLiquido>= 646920.0096 and SueldoLiquido <=1405972.8 : 
		Factor = 0.04
		CantidadRebajar = 25876.80

	elif SueldoLiquido>= 1405972.8092 and SueldoLiquido <= 2287700.8: 
		Factor = 0.08
		CantidadRebajar = 83380.80

	elif SueldoLiquido>= 2287700.80865 and SueldoLiquido <= 3116716.8: 
		Factor = 0.135
		CantidadRebajar = 215160.80

	elif SueldoLiquido>= 3116716.8072 and SueldoLiquido <= 3854684.8: 
		Factor = 0.23
		CantidadRebajar = 533828.80

	elif SueldoLiquido>= 3854684.80696 and SueldoLiquido <= 4855254.4: 
		Factor = 0.304
		CantidadRebajar = 852976

	elif SueldoLiquido>= 4855254.4065: 
		Factor = 0.35
		CantidadRebajar = 1117494.40


	afp = request.form["afp"]
	if afp == 'Capital' :
		afp = 12.97
	elif afp == 'Cuprum' :
		afp = 12.97
	elif afp == 'Habitat' :
		afp = 12.80
	elif afp == 'PlanVital' :
		afp = 12.69
	elif afp == 'ProVida' :
		afp = 12.98
	elif afp == 'Modelo' :
		afp = 12.30

	LiquidoImponible = (SueldoLiquido - CantidadRebajar) / (1-Factor)

	SueldoBruto = LiquidoImponible / (1- (7/100 + afp/100 + 0.6/100) ) 



	return SueldoBruto

if __name__ == '__main__':
	app.run(debug=True,host=host,port=port)