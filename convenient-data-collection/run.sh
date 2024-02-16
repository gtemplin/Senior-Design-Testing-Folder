#!/bin/bash

docker build -t test:test .

docker run -v /home/admin/senior-design-testing-folder/local-volume:/usr/src/app/BackupData --network=hassio -it test:test /bin/bash

