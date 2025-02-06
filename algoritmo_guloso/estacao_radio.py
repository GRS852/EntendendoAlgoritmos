estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Estações que podem ser escolhidas de acordo com o estado

estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres'"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])

estacoes_final = set()