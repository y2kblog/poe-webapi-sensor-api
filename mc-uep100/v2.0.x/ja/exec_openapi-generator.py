#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from subprocess import PIPE, STDOUT
import glob


JAR_DIR_PATH = './../../../tools/openapi-generator/'
OUTPUT_LANG = ['python', 'dart']
JAR_URL = r'https://mvnrepository.com/artifact/org.openapitools/openapi-generator-cli'


def main():
    jar_path_list = [p for p in glob.glob(os.path.abspath(JAR_DIR_PATH) + '/openapi-generator-cli-*.jar') if os.path.isfile(p)]
    if len(jar_path_list) == 0:
        print(f'Not found jar file. Download OpenAPI Generator jar file from "{JAR_URL}" and place under "{os.path.abspath(JAR_DIR_PATH)}"')
        sys.exit(1)
    jar_path = sorted(jar_path_list, reverse=True)[0]
    # print(jar_path)

    yaml_path = glob.glob(os.path.dirname(os.path.abspath(sys.argv[0])) + '/*.yaml')[0]
    # print(yaml_path)

    # Validate
    cmd = ['java', '-jar',
            os.path.abspath(jar_path),
            'validate',
            '-i', yaml_path,
    ]
    print(f"Validate command: {' '.join(cmd)}")
    cp = subprocess.run(cmd, stdout=PIPE, stderr=STDOUT, text=True, encoding="shift-jis")
    if cp.returncode != 0:
        print('Failed to validate code.')
        print(cp.stdout)
        sys.exit(1)

    # generate library files
    for lang in OUTPUT_LANG:
        cmd = ['java', '-jar',
                os.path.abspath(jar_path),
                'generate', '--skip-validate-spec',
                '-i', yaml_path,
                '-g', lang,
                '-o', os.path.abspath(f"./autogen-openapi-generator/{lang}"),
        ]
        print(f"Generate Command ({lang}): {' '.join(cmd)}")
        cp = subprocess.run(cmd, stdout=PIPE, stderr=STDOUT, text=True, encoding="shift-jis")
        if cp.returncode == 0:
            print('Completed to generate code.')
        else:
            print('Failed to generate code.')
            print(cp.stdout)
            sys.exit(1)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    main()
