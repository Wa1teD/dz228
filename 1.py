def __init__(self, znam: int = 1, chis: int = 0) -> None:
	self.znam = znam
	self.chis = chis


def inner(self) -> None:
	self.chis = int(input('Введите числитель '))
	self.znam = int(input('Введите знаменатель '))
	if self.znam == 0:
		raise ZeroDivisionError


def __str__(self) -> str:
	return f"{self.chis}/{self.znam}"
	
