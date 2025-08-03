# SimplMessage.py - Kod Açıklaması

Bu belge, `simplemessage.py` dosyasının ne yaptığını adım adım açıklamaktadır.

## Genel Bakış
Bu Python scripti, OpenAI'nin GPT-4o modelini kullanarak İngilizce metinleri Türkçe'ye çeviren basit bir çeviri uygulamasıdır. LangChain framework'ü kullanarak AI modeli ile etkileşim kurar.

## Kod Analizi

### 1. Kütüphane İmportları
```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
```

**Ne yapar:**
- `dotenv`: `.env` dosyasından ortam değişkenlerini yüklemek için
- `langchain_openai`: OpenAI GPT modellerini LangChain ile kullanmak için
- `langchain_core.messages`: AI ile konuşma mesajlarını yapılandırmak için

### 2. Ortam Değişkenlerini Yükleme
```python
load_dotenv()
```

**Ne yapar:**
- `.env` dosyasındaki `OPENAI_API_KEY` ve diğer ortam değişkenlerini sistem ortamına yükler
- Bu sayede API anahtarı güvenli bir şekilde kod dışında tutulur

### 3. AI Modeli Yapılandırması
```python
model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.1
)
```

**Ne yapar:**
- OpenAI'nin GPT-4o modelini başlatır
- `temperature=0.1`: Düşük sıcaklık değeri, daha tutarlı ve tahmin edilebilir çıktılar üretir
- Yüksek sıcaklık (1.0'a yakın) daha yaratıcı ama rastgele sonuçlar verir

### 4. Konuşma Mesajlarını Tanımlama
```python
messages = [
    SystemMessage(
        content="Translate the following English text to Turkish'"
    ),
    HumanMessage(
        content="Hello, how are you?"
    )
]
```

**Ne yapar:**
- `SystemMessage`: AI'ya rolünü ve ne yapması gerektiğini söyler (İngilizce metni Türkçe'ye çevir)
- `HumanMessage`: Çevrilmek istenen İngilizce metni içerir ("Hello, how are you?")

### 5. Ana Çalıştırma Bloğu
```python
if __name__ == "__main__":
    response = model.invoke(messages)
    print(response.content)
```

**Ne yapar:**
- Script doğrudan çalıştırıldığında (import edilmediğinde) bu blok çalışır
- `model.invoke(messages)`: Hazırlanan mesajları AI modeline gönderir
- `response.content`: AI'nın ürettiği çeviri sonucunu konsola yazdırır

## Çalışma Akışı

1. **Başlatma**: Script çalıştırıldığında önce gerekli kütüphaneler yüklenir
2. **Yapılandırma**: `.env` dosyasından API anahtarı alınır ve GPT-4o modeli başlatılır
3. **Mesaj Hazırlama**: Sistem talimatı ve çevrilecek metin hazırlanır
4. **AI Çağrısı**: Hazırlanan mesajlar OpenAI API'sine gönderilir
5. **Sonuç**: AI'nın ürettiği Türkçe çeviri ekrana yazdırılır

## Örnek Çıktı
```
Merhaba, nasılsın?
```

## Gereksinimler
- Python 3.9+
- `requirements.txt` dosyasındaki tüm paketler
- `.env` dosyasında geçerli `OPENAI_API_KEY`

## Güvenlik Notları
- API anahtarı `.env` dosyasında güvenli bir şekilde saklanır
- Bu dosya `.gitignore`'a eklenmeli ve paylaşılmamalıdır
- Temperature değeri düşük tutularak tutarlı sonuçlar alınır

## Potansiyel Geliştirmeler
- Farklı dil çiftleri için destek
- Dosyadan metin okuma özelliği
- Batch çeviri desteği
- Hata yakalama ve işleme mekanizmaları
