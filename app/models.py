from django.db import models


# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название поставщика")
    address = models.CharField(max_length=300, verbose_name="Адрес поставщика")
    email = models.EmailField(verbose_name="Почта поставщика")
    phone = models.IntegerField(verbose_name="Телефон поставщика")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        db_table = 'Supplier'


class Manufacturer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название производителя")
    address = models.CharField(max_length=300, verbose_name="Адрес производителя")
    email = models.EmailField(verbose_name="Почта производителя")
    phone = models.IntegerField(verbose_name="Телефон производителя")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
        db_table = 'Manufacturer'


class Distributor(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО покупателя")
    email = models.EmailField(verbose_name="Почта покупателя")
    phone = models.IntegerField(verbose_name="Телефон покупателя")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"
        db_table = 'Distributor'


class Car(models.Model):
    car_name = models.CharField(max_length=100, verbose_name="Название машины")
    capacity = models.IntegerField(verbose_name="Вместимость машины")

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"
        db_table = 'Car'


class Storehouse(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название склада")
    address = models.CharField(max_length=300, verbose_name="Адрес склада")
    capacity = models.FloatField(verbose_name="Вместимость склада")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"
        db_table = 'Storehouse'


class MatrixType(models.Model):
    type_name = models.CharField(max_length=50, verbose_name="Тип матрицы")

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = "Тип матрицы"
        verbose_name_plural = "Типы матриц"
        db_table = "Matrix_type"


class Matrix(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название матрицы")
    contrast = models.FloatField(verbose_name="Контрастность")
    resolution = models.FloatField(verbose_name="Разрешение")
    price = models.FloatField(verbose_name="Цена матрицы")
    matrix_type = models.ForeignKey(MatrixType, on_delete=models.PROTECT, verbose_name="Тип матрицы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Матрица"
        verbose_name_plural = "Матрицы"
        db_table = "Matrix"


class Loudspeakers(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название колонок")
    count = models.IntegerField(verbose_name="Количество колонок")
    price = models.FloatField(verbose_name="Стоимость колонок")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Колонки"
        verbose_name_plural = "Колонки"
        db_table = "Loudspeakers"


class CaseBox(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название корпуса")
    price = models.FloatField(verbose_name="Стоимость корпуса")
    width = models.FloatField(verbose_name="Ширина")
    length = models.FloatField(verbose_name="Длина")
    depth = models.FloatField(verbose_name="Глубина")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Корпус"
        verbose_name_plural = "Корпусы"
        db_table = "CaseBox"


class Mainplata(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название платы")
    price = models.FloatField(verbose_name="Стоимость платы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Главная плата"
        verbose_name_plural = "Главные платы"
        db_table = "Mainplata"


class Powerboard(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название платы питания")
    price = models.FloatField(verbose_name="Стоимость платы питания")
    power = models.IntegerField(verbose_name="Мощность")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Плата питания"
        verbose_name_plural = "Платы питания"
        db_table = "Powerboard"


class Specifications(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название спецификации")
    matrix = models.ForeignKey(Matrix, on_delete=models.PROTECT, verbose_name="Матрица")
    powerboard = models.ForeignKey(Powerboard, on_delete=models.PROTECT, verbose_name="Плата питания")
    mainplata = models.ForeignKey(Mainplata, on_delete=models.PROTECT, verbose_name="Главная плата")
    loudspeakers = models.ForeignKey(Loudspeakers, on_delete=models.PROTECT, verbose_name="Колонки")
    casebox = models.ForeignKey(CaseBox, on_delete=models.PROTECT, verbose_name="Корпус")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Спецификация"
        verbose_name_plural = "Спецификации"
        db_table = "Specifications"


class TV(models.Model):
    tv_model = models.CharField(max_length=150, verbose_name="Модель телевизора")
    price = models.FloatField(verbose_name="Цена телевизора")
    specification = models.ForeignKey(Specifications, on_delete=models.PROTECT, verbose_name="Спецификация")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, verbose_name="Производитель")

    def __str__(self):
        return self.tv_model

    class Meta:
        verbose_name = "Телевизор"
        verbose_name_plural = "Телевизоры"
        db_table = "TV"


class Stocks(models.Model):
    stock_count = models.IntegerField(verbose_name="Остаток")
    tv = models.ForeignKey(TV, on_delete=models.CASCADE, verbose_name="Модель телевизора")
    storehouse = models.ForeignKey(Storehouse, on_delete=models.CASCADE, verbose_name="Склад")

    # def __str__(self):
    #     return self.tv

    class Meta:
        verbose_name = "Остатки"
        verbose_name_plural = "Остатки"
        db_table = "Stocks"


class StaffStorage(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО сотрудника")
    position = models.CharField(max_length=100, verbose_name="Должность")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Сотрудник склада"
        verbose_name_plural = "Сотрудники склада"
        db_table = "Staff_storage"


class Supply(models.Model):
    tv = models.ForeignKey(TV, on_delete=models.CASCADE, verbose_name="Компонент")
    count = models.IntegerField(verbose_name="Количество")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата приемки", blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Поставщик")
    staff = models.ForeignKey(StaffStorage, on_delete=models.CASCADE, verbose_name="Сотрудник")
    storehouse = models.ForeignKey(Storehouse, on_delete=models.CASCADE, verbose_name="Склад")

    # def __str__(self):
    #     return self.supplier

    class Meta:
        verbose_name = "Приемка"
        verbose_name_plural = "Приемки"
        db_table = "Supply"


class StaffConstructor(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО сотрудника")
    position = models.CharField(max_length=100, verbose_name="Должность")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Сотрудник цеха"
        verbose_name_plural = "Сотрудники цеха"
        db_table = "Staff_constructor"


class BuildLine(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название линии")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сборочная линия"
        verbose_name_plural = "Сборочные линии"
        db_table = "build_line"


class Build(models.Model):
    build_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата сборки")
    count = models.IntegerField(verbose_name="Количество")
    tv = models.ForeignKey(TV, on_delete=models.CASCADE, verbose_name="Модель телевизора")
    line = models.ForeignKey(BuildLine, on_delete=models.CASCADE, verbose_name="Сборочная линия")
    staff = models.ForeignKey(StaffConstructor, on_delete=models.CASCADE, verbose_name="Сборщик")

    # def __str__(self):
    #     return self.build_date + self.tv

    class Meta:
        verbose_name = "Сборка"
        verbose_name_plural = "Сборки"
        db_table = "build"


class Shipment(models.Model):
    tv = models.ForeignKey(TV, on_delete=models.CASCADE, verbose_name="Товар")
    count = models.IntegerField(verbose_name="Количество")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата отгрузки")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Машина доставки")
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, verbose_name="Покупатель")
    staff = models.ForeignKey(StaffStorage, on_delete=models.CASCADE, verbose_name="Сотрудник")
    storehouse = models.ForeignKey(Storehouse, on_delete=models.CASCADE, verbose_name="Склад")

    # def __str__(self):
    #     return self.date + self.distributor

    class Meta:
        verbose_name = "Отгрузка"
        verbose_name_plural = "Отгрузки"
        db_table = "shipment"
