# Travelling Salesman Problem
TSP, Traveling Salesman Problem'in kısaltmasıdır ve bir bilgisayar programı tarafından çözülebilir bir matematiksel problemi temsil eder. Bu problem, bir satıcının bir dizi şehri ziyaret etmesi ve sonra başlangıç noktasına geri dönmesi gerektiğini varsayar. Satıcının ziyaret etmesi gereken şehirler arasındaki mesafeler ve zamanları bilinen bir durumdur.

TSP'nin bir örneğini ele alalım: Bir satıcının şehirler arasında seyahat yapması gerektiğini ve her bir şehri tam olarak bir kez ziyaret etmesi gerektiğini varsayalım. Bu durumda, satıcının hangi şehirleri ne sırayla ziyaret etmesi gerektiği, minimum toplam mesafeyi veya en az toplam geçiş süresini bulmayı içerir.

Bu sorun genellikle bir grafik modeli olarak ifade edilir: Şehirler örneklemelerdir ve şehirler arasındaki mesafeler köşeler arasındaki ağırlıklardır. Bu model, TSP'nin bir NP-Tam problemi olmasının nedeni olup, çözümünün zaman karmaşıklığı O(2^n) olmasına neden olur, burada n şehir sayısıdır. Bu, çözümün büyük örnekler için uygulanabilir olmadığı anlamına gelir.

TSP'nin birçok uygulaması vardır, örneğin logistikte ve operasyonel araştırmada. Örneğin, bir satıcının bir dizi mağazayı ziyaret etmesi ve sonra merkeze geri dönmesi gerektiği durumlarda, TSP'yi kullanarak satıcının hangi mağazaları ne sırayla ziyaret etmesi gerektiğini belirleyebiliriz.

