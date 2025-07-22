Para extraer los fotogramas de un video: lanzar el terminal desde esta carpeta e introducir 
el siguiente comando modificando los parámetros adecuadamente:

ffmpeg -ss 00:00 -i Scene9SCC42B.avi -t 00:22 frame_Scene9SCC42B-%03d.jpg

(modificar Scene9SCC42B.avi por el nombre del video, 00:22 por la duración en segundos del
video y frame_ "Scene9SCC42B" -%03d.jpg por el nombre del video)
