
class Testcase:

	def sub_mult(self,a,b):
		return (a - b) * 2

	def add_mult(self,a,b):
		return (a + b) * 2

	def mult_mult(self,a,b):
		return (a * b) * 2

	def div_mult(self,a,b):
		return (a / b) * 2

###########################################

	def sub_add(self,a,b):
		return (a - b) + 2

	def add_add(self,a,b):
		return (a + b) + 2

	def mult_add(self,a,b):
		return (a * b) + 2

	def div_add(self,a,b):
		return (a / b) + 2

###########################################

	def sub_sub(self,a,b):
		return (a - b) - 2

	def add_sub(self,a,b):
		return (a + b) - 2

	def mult_sub(self,a,b):
		return (a * b) - 2

	def div_sub(self,a,b):
		return (a / b) - 2

##########################################

	def sub_div(self,a,b):
		return (a - b) / 2

	def add_div(self,a,b):
		return (a + b) / 2

	def mult_div(self,a,b):
		return (a * b) / 2

	def div_div(self,a,b):
		return (a / b) / 2


TestCase = Testcase()

output = []
int = -2000
correct_arith = 0
incorrect_arith = 0


while int < 2000:
	
	int = int + 1
	correct_arith = TestCase.sub_mult(int, 1)

	incorrect_arith = TestCase.add_mult(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue
	incorrect_arith = TestCase.mult_mult(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue
	incorrect_arith = TestCase.div_mult(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue
	incorrect_arith = TestCase.sub_add(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue
	incorrect_arith = TestCase.add_add(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue
	incorrect_arith = TestCase.mult_add(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue
	incorrect_arith = TestCase.div_add(int, 1)
	if (correct_arith == incorrect_arith):
		print(int)
		output.append(int)
		continue
	incorrect_arith = TestCase.sub_sub(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue
	incorrect_arith = TestCase.add_sub(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue
	incorrect_arith = TestCase.mult_sub(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue
	incorrect_arith = TestCase.div_sub(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue
	incorrect_arith = TestCase.sub_div(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue
	incorrect_arith = TestCase.add_div(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue
	incorrect_arith = TestCase.mult_div(int, 1)
	if (correct_arith == incorrect_arith):
		print(int)
		output.append(int)
		continue
	incorrect_arith = TestCase.div_div(int, 1)
	if (correct_arith == incorrect_arith):
		output.append(int)
		continue

for i in output:
	print(i)

	

