# JohnnyTheTrashFinder
Anwendung, die Abfall auf Bildern erkennen kann.
## Idee und Vision
Die Verschmutzung der Umwelt, insbesondere der Strände und Meere, durch Abfall ist ein immer größers Problem. 
Um den Müll zu beseittigen, muss erst einmal geschaut werden, wo überall Trash zu finden ist.
Das Ziel von JohnnyTheTashFinder ist es eine Heat-Map zu erstellen, auf der die Verschmutzung eingetragen ist. 
Eine Drohne soll dann entsprechend dieser Karte zu den Verschmutzungen fliegen und aufräumen.
## Umsetzung
### Brainstorming
Zunächst müssen wir viele Bilder haben, auf denen Müll zu sehen ist und auch welche, auf denen keiner zu sehen ist. 
Um zu erkennen, ob auf den Bildern Müll zu sehen ist, wollen wir ein neuronales Netzwerk benutzen. 
In einem zweiten Schritt wollen wir die Metadaten der Bilder analysieren und so die Bilder einem Standort zuordnen, sodass eine Heatmap entstehen kann. Dazu könnten wir auch OpenStreetMap nutzen.
Im dritten Schritt können wir dann eine Drohne mit der entwickelten Software ausstatten und dann Testen.
### Deep learning
image classification von Google über transfer learning auf unser Problem übertragen, sodass es am Ende möglich ist, die Bilder als dreckig oder sauber zu deklarieren.
Datensätze mit Bildern herunterladen.
## Aufgaben und Probleme
viele viele Bilder
evt. Schnittstelle mit Umweltschutzapp
Heatmap
Verbindung mit OpenStreetMap
Drohne 
## Status
02-06-2018 Anfang des Projektes, deep learning 
## Links
### Examplecode von Tensorflow ->Grundlage für Projekt
https://github.com/tensorflow/hub/raw/r0.1/examples/image_retraining/retrain.py
### Deep Learning dataset
https://github.com/garythung/trashnet
