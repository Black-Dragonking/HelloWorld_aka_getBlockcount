# bitcoinrpc importieren
from bitcoinrpc.authproxy import AuthServiceProxy

# Variablen setzen mit Werten aus der defi.conf 
RPC_USERNAME = "dein Username aus der defi.conf"
RPC_PASSWORD = "dein Passwort aus der defi.conf"
RPC_HOSTNAME = "127.0.0.1"
RPC_PORT = 8554     # Port steht auch in der defi.conf
WALLET = "deine Walletadresse von der Desktopwallet"
WALLET_PASSWORD = "dein Passwort zum entsperren der Desktopwallet"

# Zugriff auf die Desktopwallet
url = f'http://{RPC_USERNAME}:{RPC_PASSWORD}@{RPC_HOSTNAME}:{RPC_PORT}'
rpc_conn = AuthServiceProxy(url)

# Die Variable blockcount wird durch den befehl getblockcount gesetzt. Das getblockcount ist ein API Befehl, der auf der Desktopwallet in der Konsole manuell ausgeführt werden kann.
# Das Skript mach dies, in dem rpc_conn gefolgt von einem Punkt vor dem Befehl geschrieben wird.
blockcount = rpc_conn.getblockcount()

# Ausgabe des Blockcounts
print(blockcount)

# Zur Vollständigkeit hier noch der Teil, mit dem die Wallet entsperrt wird. Ist für dieses Beispiel nicht notwendig, daher auskommentiert.
# Durch diesen Befehl wird die Wallet für 60 Sekunden entsperrt.
# unlock = rpc_conn.walletpassphrase(WALLET_PASSWORD, 60)
