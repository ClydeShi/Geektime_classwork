#读取yaml文件数据
import yaml

class Runyaml:
    @classmethod
    def run_yaml(cls,yaml_path):
        return yaml.safe_load(open(yaml_path))

if __name__ == '__main__':
    print(Runyaml.run_yaml("../testcases/testdata.yaml"))