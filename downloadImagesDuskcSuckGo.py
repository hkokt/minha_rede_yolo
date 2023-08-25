import DuckDuckGoImages as ddg

filtro = "lâmpada"
destino = "workspaces/data"

print("iniciando dowloads... ")
try:
    ddg.download(filtro, folder=destino, remove_folder=False, parallel=True)
except Exception as e:
    print("type error: ", e)
print("Downloads finalizados")
