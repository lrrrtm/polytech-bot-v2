def move_env_vars():
    """Переносит названия переменных окружения из .env в .env.dist без значений"""

    with open("../.env", "r") as env_file:
        sensetive_data = env_file.readlines()

    sensetive_data = list(filter(lambda line: line != "\n" and line[0] != ';', sensetive_data))

    clear_vars = "\n".join([line.split("=")[0] + "=" for line in sensetive_data])

    with open("../.env.dist", "w") as dist_file:
        dist_file.writelines(clear_vars)


if __name__ == "__main__":
    move_env_vars()
