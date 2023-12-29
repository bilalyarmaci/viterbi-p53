# viterbi-p53
**Viterbi Algoritması** genellikle **Saklı Markov Modelleri** (SMM) ile ilişkilendirilir; zaman serileriyle ilgili problemleri çözmek için kullanılan bir dinamik programlama algoritmasıdır. SMM de gözlemler arasında gizlice değişen durumların olduğu bir modeldir.

**Amacı**, eğitilmiş bir modele ve gözlemlenen bazı verilere dayanarak çıkarım yapmaktır. Şu soruyu sorarak çalışır: ‘_Verilere ve eğitilen modele göre en olası seçim nedir?’_. Cevap da verilere bağlı olarak belirlenir. **Özellikle** konuşma tanıma, doğal dil işleme ve biyoinformatik gibi birçok uygulama alanında kullanılmaktadır.

Algoritma Analizi ve Tasarımı dersi için hazırladığım çalışmada da P53 DNA dizisi (insanlarda kanserle ilişkili olan bir genin DNA dizisi) üzerinde Viterbi Algoritması'nı uygulamak için özel bir model inceledim. Özet olarak hazırlanan örnek çalışmada P53 DNA dizisi üzerinde Viterbi Algoritması ile durum tahmini yapılmaya çalışılmıştır. Kullanılan veriler örnek veri olup gerçek hayat problemleri için gerçek hayat verileri kullanılması gerekmektedir. Bu çalışma özellikle kanser tespiti için çok önemli olan bu kullanım alanını örneklemektedir.
