# 1. TASK: print "Hola, mundo"
print("Hola, mundo")

# 2. print "Hola Noelle!" con el nombre de una variable
name = "Jaime"
print("Hola", name)	# con una coma
print("Hola" + name)	# con un +

# 3. print "Hola 42!" con el número en una variable
name = 42
print("Hola ", name)	# con una coma
print("Hola " + name)	# con un +	-- ¡esta nos debería arrojar un error!

# 4. print "Amo comer sushi y pizza." con las comidas en variables
fave_food1 = "hotdog"
fave_food2 = "pizza"
print("Amo comer {} y {}".format(fave_food1, fave_food2)) # with .format()
print(f"Amo comer {fave_food1} y {fave_food2}.") # with an f string

