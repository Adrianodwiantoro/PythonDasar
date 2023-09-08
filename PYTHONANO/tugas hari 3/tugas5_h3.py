import turtle

# Membuat objek Turtle
pen = turtle.Turtle()

# Fungsi untuk menggambar petal (kelopak)
def petal(radius):
    pen.circle(radius, 60)
    pen.left(120)
    pen.circle(radius, 60)

# Fungsi untuk menggambar bunga mawar
def rose_flower(petals, petal_length):
    for _ in range(petals):
        petal(petal_length)
        pen.left(360 / petals)

# Set kecepatan gambar
pen.speed(0)

# Pindahkan pena ke posisi awal
pen.penup()
pen.goto(0, -200)
pen.pendown()

# Gambar bunga mawar dengan 6 kelopak
rose_flower(6, 100)

# Tutup jendela gambar saat selesai
turtle.done()