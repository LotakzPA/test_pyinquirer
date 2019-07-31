from config import configs_var

def generate_config(configs_var, file_name):
    with open(file_name, 'r') as config_template:
        spamreader = config_template.read()
        conf_file_name = file_name[:-5]
        nginx_config = spamreader.format(**configs_var)

        with open("generate/"+conf_file_name, "w") as nginx_conf:
            nginx_conf.write(nginx_config)


generate_config(configs_var, "nginx.conf.tmpl")
