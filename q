[0;1;32m●[0m mongod.service - MongoDB Database Server
     Loaded: loaded (/lib/systemd/system/mongod.service; disabled; vendor preset: enabled)
     Active: [0;1;32mactive (running)[0m since Sun 2024-04-07 23:40:25 IST; 6s ago
       Docs: https://docs.mongodb.org/manual
   Main PID: 112249 (mongod)
     Memory: 177.1M
     CGroup: /system.slice/mongod.service
             └─112249 /usr/bin/mongod --config /etc/mongod.conf

Apr 07 23:40:25 aspire-a514-54g systemd[1]: Started MongoDB Database Server.
Apr 07 23:40:25 aspire-a514-54g mongod[112249]: {"t":{"$date":"2024-04-07T18:10:25.499Z"},"s":"I",  "c":"CONTROL",  "id":7484500, "ctx":"main","msg":"Environment variable MONGODB_CONFIG_OVERRIDE_NOFORK == 1, overriding \"processManagement.fork\" to false"}
