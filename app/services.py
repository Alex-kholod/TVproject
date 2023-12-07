from .models import TV, Supply, Shipment, Stocks


# Функции получения данных и передачи в представления
def get_models_tv():
    data_list = []
    keys_list = []
    for row in TV.objects.all():
        data_dict = {
            "ID": row.id,
            "Модель": row.tv_model,
            "Стоимость": row.price,
            "Спецификация": row.specification,
            "Производитель": row.manufacturer
        }
        data_list.append(data_dict)
        keys_list = data_dict.keys()
    data = {
        "data_list": data_list,
        "keys_list": keys_list
    }
    return data


def get_supplies():
    data_list = []
    keys_list = []
    for row in Supply.objects.all().order_by('-date'):
        data_dict = {
            "Дата приемки": row.date,
            "Модель телевизора": row.tv,
            "Количество": row.count,
            "Поставщик": row.supplier,
            "Сотрудник": row.staff
        }
        data_list.append(data_dict)
        keys_list = data_dict.keys()
    data = {
        "data_list": data_list,
        "keys_list": keys_list,
        "button_name": "создать приемку"
    }
    return data


def get_stocks():
    data_list = []
    keys_list = []
    for row in Stocks.objects.all():
        data_dict = {
            "Модель телевизора": row.tv,
            "Склад": row.storehouse,
            "Остаток": row.stock_count
        }
        data_list.append(data_dict)
        keys_list = data_dict.keys()
    data = {
        "data_list": data_list,
        "keys_list": keys_list
    }
    return data


def get_shipments():
    data_list = []
    keys_list = []
    for row in Shipment.objects.all():
        data_dict = {
            "Дата создания": row.date,
            "Модель телевизора": row.tv,
            "Количество": row.count,
            "Покупатель": row.distributor,
            "Сотрудник": row.staff,
            "Машина": row.car
        }
        data_list.append(data_dict)
        keys_list = data_dict.keys()
    data = {
        "data_list": data_list,
        "keys_list": keys_list,
        "button_name": "создать отгрузку"
    }
    return data


# Функции добавления данных в базу данных

def add_stock(count, tv, storehouse):
    is_exists = Stocks.objects.filter(storehouse=storehouse.pk).contains(tv)
    if is_exists:
        row = Stocks(id=tv.pk)
        row.stock_count += count
        row.save()
    else:
        Stocks(tv=tv, stock_count=count, storehouse=storehouse).save()


def update_stock(count, tv, storehouse):
    is_exists = Stocks.objects.filter(storehouse=storehouse.pk).contains(tv)
    if is_exists:
        row = Stocks(id=tv.pk)
        row.stock_count -= count
        row.save()
    else:
        print("Вы не можете отгрузить товар, которого нет")