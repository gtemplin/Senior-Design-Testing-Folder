#!/bin/bash

docker build -t test:test .

docker run --name test -v /home/admin/senior-design-testing-folder/local-volume:/usr/src/app/BackupData -it test:test #/bin/bash

# --network=host 