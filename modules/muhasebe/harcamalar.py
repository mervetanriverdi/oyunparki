def harcama_ekle(harcama_turu, miktar, tarih):
    """
    Harcamayı ekler.
    
    :param harcama_turu: Harcamanın türü (örneğin, 'personel', 'malzeme', 'bakim')
    :param miktar: Harcama miktarı (int veya float)
    :param tarih: Harcamanın yapıldığı tarih (str, 'YYYY-MM-DD' formatında olmalı)
    :return: Harcama kaydını içeren sözlük
    """
    harcama = {
        "harcama_turu": harcama_turu,
        "miktar": miktar,
        "tarih": tarih
    }
    return harcama
