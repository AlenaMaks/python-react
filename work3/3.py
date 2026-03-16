# 3 задание

# разный вид типизации у args и kwargs по историческим причинам :)
def function_name(search: str, status: bool, *args: tuple[any, ...], **kwargs: any) -> list[int] | str:
    """Выполняет действия в зависимости от переданной команды и аргументов
    search - принимает строку args/kwargs, зависит будет работать с данными как с кортежем или словарем
    status - принимает значение True/False, имеет влияние только при args, при True работает только с числами,
    при False работает со всеми типами как со строкой
    *args/**kwargs передача аргументов
    
    raise ValueError("Error for search") - в случае если search предоставлено не одним из обрабатываемых значений"""
    result: list[int] = []
    result_2: str = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")
    
help(function_name)
print(function_name('kwargs', 0, a=10, b=20))
print(function_name('args', 1, 1, 2, "hi", 4, 6))