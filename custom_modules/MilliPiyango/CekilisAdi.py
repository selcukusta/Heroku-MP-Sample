class CekilisAdi(object):
    @staticmethod
    def GetName(slug):
        if slug == "sayisal":
            return "Sayısal Loto"
        elif slug == "onnumara":
            return "On Numara"
        elif slug == "sanstopu":
            return "Şans Topu"
        elif slug == "superloto":
            return "Süper Loto"
        else:
            return ""