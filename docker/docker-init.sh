#!/usr/bin/env bash

#!/usr/bin/env bash

TRY_LOOP="20"

: "${POSTGRES_HOST:="postgres"}"
: "${POSTGRES_PORT:="5432"}"

wait_for_port() {
  local name="$1" host="$2" port="$3"
  local j=0
  while ! nc -z "$host" "$port" >/dev/null 2>&1 < /dev/null; do
    j=$((j+1))
    if [ $j -ge $TRY_LOOP ]; then
      echo >&2 "$(date) - $host:$port still not reachable, giving up"
      exit 1
    fi
    echo "$(date) - waiting for $name... $j/$TRY_LOOP"
    sleep 5
  done
}


wait_for_port "Postgres" "$POSTGRES_HOST" "$POSTGRES_PORT"

echo "running INIT DB"

/opt/odoo-bin \
--db_host=$POSTGRES_HOST \
--db_user=$POSTGRES_USER \
--database=$POSTGRES_DB \
--db_port=$POSTGRES_PORT \
--db_password=$POSTGRES_PASSWORD \
--data-dir=/opt/odoo_data_dir \
--addons-path=/opt/addons,/opt/odoo/addons,/opt/refy_addons \
--init=base,crm \
--without-demo=all \
--log-request \
--log-handler=odoo.http.rpc.request:DEBUG \
--log-handler=odoo.http.rpc.response:DEBUG



