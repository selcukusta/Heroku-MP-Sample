from custom_modules.MilliPiyango.Cekilis import Cekilis
from custom_modules.MilliPiyango.CekilisAdi import CekilisAdi

class MPParser(object):
    def __init__(self, result):
        self.JObject = result

    def GetCekilisSonuclari(self, cekilisTipi):
        numbers = []
        date = ""
        title = ""
        if self.JObject is None or cekilisTipi not in self.JObject:
            return None

        json_sayisal_object = self.JObject[cekilisTipi]
        if json_sayisal_object is None or "rakamlar" not in json_sayisal_object or "tarih" not in json_sayisal_object:
            return None

        json_sayisal_rakamlar_object = str(json_sayisal_object["rakamlar"]).split("-")
        if json_sayisal_rakamlar_object is None or len(json_sayisal_rakamlar_object) <= 0:
            return None

        date = json_sayisal_object["tarih"]
        title = CekilisAdi.GetName(cekilisTipi)
        numbers = []
        for rakam in json_sayisal_rakamlar_object:
            numbers.append(rakam.strip())

        return Cekilis(numbers, date, title)
        