import numpy as np

def viterbi_p53(sequence):
    # Durumlar: "Normal", "Mutasyon"
    states = ["Normal", "Mutasyon"]

    # Başlangıç olasılıkları
    initial_probs = [0.5, 0.5]

    # Durum geçiş olasılıkları
    transition_probs = np.array([[0.8, 0.2], [0.1, 0.9]])

    # Gözlem olasılıkları
    emission_probs = {
        "Normal": {"A": 0.3, "T": 0.3, "G": 0.2, "C": 0.2},
        "Mutasyon": {"A": 0.1, "T": 0.2, "G": 0.1, "C": 0.6}
    }

    # Gözlem dizisi
    observations = list(sequence)

    # Gözlem serisinin uzunluğu
    T = len(observations)
    # Durum kümesinin uzunluğu (Normal ve Mutasyon => 2)
    K = len(states)

    # T1 (ileri geçiş) ve T2 (geriye geçiş) matrisleri
    T1 = np.zeros((K, T))
    T2 = np.zeros((K, T), dtype=int)

    # İlk zaman adımı için hesaplamalar
    for i in range(K):
        T1[i, 0] = initial_probs[i] * emission_probs[states[i]][observations[0]]
        T2[i, 0] = 0

    # Geriye doğru hesaplama
    for j in range(1, T):
        for i in range(K):
            values = [T1[k, j-1] * transition_probs[k, i] * emission_probs[states[i]][observations[j]] for k in range(K)]
            T1[i, j] = max(values)
            T2[i, j] = np.argmax(values)

    # En olası durumu ve durum serisini bul
    z_T = np.argmax(T1[:, T-1]) # Gözlem serisinin sonunda, en olası durumu belirleyerek indeksini z_T değişkenine ata
    x_T = [states[z_T]]         # indekse karşılık gelen durumu, yani en olası durumu, x_T listesine ekle

    for j in range(T-1, 0, -1): # Seriyi son gözlemden başlayarak, ilk gözleme kadar geri dönerek adım yapar.
        z_T = T2[z_T, j]        # Matrisi kullanarak bir önceki zaman adımında en olası durumu belirler.
        x_T.insert(0, states[z_T]) # İndekse karşılık gelen durumu, yani en olası durumu, x_T listesinin başına ekler.

    return x_T

# örnek P53 DNA dizisi
p53_sequence = "ATGCGTCTC"

# VİTERBİ ALGORİTMASI UYGULAMASI
i_type = int(input("Kendi DNA dizinizi girmek için '1', örnek sekans için '0' giriniz: ").strip())
if(i_type):
    p53_sequence = input("DNA dizisi: ")
result = viterbi_p53(p53_sequence)
print("En olası durum serisi:", result)
