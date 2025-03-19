

def harcama_ekle(harcama_turu, miktar, tarih):
    """
    Harcamayı ekler.
    :param harcama_turu: Harcamanın türü (örneğin, 'personel', 'malzeme', 'bakim')
    :param miktar: Harcama miktarı
    :param tarih: Harcamanın yapıldığı tarih
    :return: Harcama kaydını döndürür
    """
    harcama = {
        "harcama_turu": harcama_turu,
        "miktar": miktar,
        "tarih": tarih
    }
    return harcama

