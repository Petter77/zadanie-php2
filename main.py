import tkinter as tk
import math
import random


class UFO:
    """Klasa reprezentująca obiekt UFO."""

    def __init__(self, _id, _x, _y):
        """
        Inicjalizacja obiektu UFO.

        :param _id: Unikalny identyfikator obiektu UFO.
        :param _x: Współrzędna X środka obiektu UFO.
        :param _y: Współrzędna Y środka obiektu UFO.
        """
        self._id = _id
        self._x = _x
        self._y = _y

    @property
    def id(self):
        """Zwraca identyfikator obiektu UFO."""
        return self._id

    @property
    def x(self):
        """Zwraca współrzędną X środka obiektu UFO."""
        return self._x

    @property
    def y(self):
        """Zwraca współrzędną Y środka obiektu UFO."""
        return self._y

    @id.setter
    def id(self, new_id):
        """Ustawia nowy identyfikator obiektu UFO."""
        self._id = new_id

    @x.setter
    def x(self, new_x):
        """Ustawia nową współrzędną X środka obiektu UFO."""
        self._x = new_x

    @y.setter
    def y(self, new_y):
        """Ustawia nową współrzędną Y środka obiektu UFO."""
        self._y = new_y


def draw_circle():
    """
    Rysuje okrąg reprezentujący obiekt UFO.

    :return: Obiekt UFO.
    """
    # Pobierz aktualne współrzędne środka płótna
    center_x = windowWidth // 2
    center_y = windowHeight // 2

    # Rysuj okrąg na płótnie w środku
    circle_radius = 30
    global ufo  # Dodaj globalną deklarację, aby ufo było dostępne w innych funkcjach
    ufo = UFO(canvas.create_oval(center_x - circle_radius, center_y - circle_radius,
                                 center_x + circle_radius, center_y + circle_radius,
                                 fill="#222222", outline="#ffffff"), center_x, center_y)
    return ufo


def move_ufo():
    """
    Przenosi obiekt UFO w nowe miejsce po kliknięciu.

    :return: None.
    """
    global selected_ufo
    selected_ufo = None
    print("Kliknij na UFO, które chcesz przesunąć.")

    # Przypisz funkcję on_ufo_click do obsługi kliknięcia na UFO
    canvas.bind('<Button-1>', on_ufo_click)


def on_ufo_click(event):
    """
    Obsługuje kliknięcie na obiekt UFO.

    :param event: Zdarzenie kliknięcia myszy.
    :return: None.
    """
    global selected_ufo
    # Sprawdź, czy kliknięto na któryś z obiektów UFO
    ufo_item = canvas.find_closest(event.x, event.y)
    if ufo_item:
        selected_ufo = ufo_item[0]
        print(f"Kliknięto na UFO o ID: {selected_ufo}")
        canvas.unbind('<Button-1>')  # Zakończ nasłuchiwanie kliknięć po wyborze UFO
        print("Kliknij na nową lokalizację dla UFO.")
        # Przypisz funkcję on_canvas_click do obsługi kliknięcia na nową lokalizację
        canvas.bind('<Button-1>', on_canvas_click)


def on_canvas_click(event):
    """
    Obsługuje kliknięcie na płótno w celu przesunięcia obiektu UFO.

    :param event: Zdarzenie kliknięcia myszy.
    :return: None.
    """
    global selected_ufo
    if selected_ufo is not None:
        x, y = event.x, event.y
        canvas.move(selected_ufo, x - ufo.x, y - ufo.y)  # Przesuń obiekt UFO do nowej lokalizacji
        current_x, current_y, _, _ = canvas.coords(selected_ufo)
        dx, dy = x - current_x, y - current_y
        ufo.x = current_x  # Zaktualizuj współrzędną X obiektu UFO
        ufo.y = current_y  # Zaktualizuj współrzędną Y obiektu UFO
        print(f"Przesunięto UFO o ID {selected_ufo} o wektor dX={dx}, dY={dy} do lokalizacji: X={current_x}, Y={current_y}")
        selected_ufo = None  # Zresetuj wybrane UFO po przesunięciu
        canvas.unbind('<Button-1>')  # Zakończ nasłuchiwanie kliknięć po przesunięciu UFO


def check_position():
    """
    Sprawdza aktualne położenie obiektu UFO po kliknięciu.

    :return: None.
    """
    global selected_ufo
    selected_ufo = None
    print("Kliknij na UFO, którego położenie chcesz sprawdzić.")

    # Przypisz funkcję on_check_position_click do obsługi kliknięcia na UFO
    canvas.bind('<Button-1>', on_check_position_click)


def on_check_position_click(event):
    """
    Obsługuje kliknięcie w celu sprawdzenia położenia obiektu UFO.

    :param event: Zdarzenie kliknięcia myszy.
    :return: None.
    """
    global selected_ufo
    # Sprawdź, czy kliknięto na któryś z obiektów UFO
    ufo_item = canvas.find_closest(event.x, event.y)
    if ufo_item:
        selected_ufo = ufo_item[0]
        x, y, _, _ = canvas.coords(selected_ufo)
        print(f"Aktualna pozycja UFO o ID {selected_ufo}: X={x}, Y={y}")
        canvas.unbind('<Button-1>')  # Zakończ nasłuchiwanie kliknięć po sprawdzeniu pozycji UFO


def calculate_distance():
    """
    Oblicza odległość między dwoma obiektami UFO po kliknięciu.

    :return: Odległość między obiektami UFO.
    """
    global selected_ufo1, selected_ufo2
    selected_ufo1 = None
    selected_ufo2 = None
    print("Kliknij na pierwsze UFO.")

    # Przypisz funkcję on_first_ufo_click do obsługi kliknięcia na pierwsze UFO
    canvas.bind('<Button-1>', on_first_ufo_click)


def on_first_ufo_click(event):
    """
    Obsługuje kliknięcie na pierwsze UFO w celu obliczenia odległości.

    :param event: Zdarzenie kliknięcia myszy.
    :return: None.
    """
    global selected_ufo1
    # Sprawdź, czy kliknięto na któryś z obiektów UFO
    ufo_item = canvas.find_closest(event.x, event.y)
    if ufo_item:
        selected_ufo1 = ufo_item[0]
        print(f"Kliknięto na pierwsze UFO o ID: {selected_ufo1}")
        canvas.unbind('<Button-1>')  # Zakończ nasłuchiwanie kliknięć po wyborze pierwszego UFO
        print("Kliknij na drugie UFO.")
        # Przypisz funkcję on_second_ufo_click do obsługi kliknięcia na drugie UFO
        canvas.bind('<Button-1>', on_second_ufo_click)


def on_second_ufo_click(event):
    """
    Obsługuje kliknięcie na drugie UFO w celu obliczenia odległości.

    :param event: Zdarzenie kliknięcia myszy.
    :return: None.
    """
    global selected_ufo1, selected_ufo2
    # Sprawdź, czy kliknięto na któryś z obiektów UFO
    ufo_item = canvas.find_closest(event.x, event.y)
    if ufo_item:
        selected_ufo2 = ufo_item[0]
        print(f"Kliknięto na drugie UFO o ID: {selected_ufo2}")
        canvas.unbind('<Button-1>')  # Zakończ nasłuchiwanie kliknięć po wyborze drugiego UFO

        # Oblicz odległość między UFO
        distance = calculate_distance_between_ufo(selected_ufo1, selected_ufo2)
        print(f"Odległość między UFO o ID {selected_ufo1} a UFO o ID {selected_ufo2}: {distance}")


def calculate_distance_between_ufo(ufo_id1, ufo_id2):
    """
    Oblicza odległość między dwoma obiektami UFO.

    :param ufo_id1: Identyfikator pierwszego obiektu UFO.
    :param ufo_id2: Identyfikator drugiego obiektu UFO.
    :return: Odległość między obiektami UFO.
    """
    x1, y1, _, _ = canvas.coords(ufo_id1)
    x2, y2, _, _ = canvas.coords(ufo_id2)
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def randomize_ufo():
    """
    Przemieszcza obiekty UFO na losowe pozycje.

    :return: None.
    """
    print("Przelosuj UFO")
    for ufo_id in canvas.find_all():
        new_x = random.randint(0, windowWidth)
        new_y = random.randint(0, windowHeight)

        # Pobierz aktualne rozmiary UFO
        x1, y1, x2, y2 = canvas.coords(ufo_id)
        width = x2 - x1
        height = y2 - y1

        # Ustaw nowe współrzędne z uwzględnieniem środka obiektu
        canvas.coords(ufo_id, new_x - width / 2, new_y - height / 2, new_x + width / 2, new_y + height / 2)

        print(f"Przelosowano UFO o ID {ufo_id} do lokalizacji: X={new_x}, Y={new_y}")


windowWidth = 800
windowHeight = 800

root = tk.Tk()
root.title("Collision Resolution")

canvas = tk.Canvas(root, width=windowWidth, height=windowHeight, bg="#222222", highlightthickness=0)
canvas.pack()


# Kontener na przyciski
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP)

# Dodaj przyciski do kontenera i przypisz funkcje do zdarzenia naciśnięcia przycisku
button_draw_circle = tk.Button(button_frame, text="Narysuj okrąg", command=draw_circle)
button_draw_circle.pack(side=tk.LEFT, padx=5)

# Przykład użycia funkcji move_ufo przy przycisku
button_move_ufo = tk.Button(button_frame, text="Przesuń UFO", command=move_ufo)
button_move_ufo.pack(side=tk.LEFT, padx=5)

button_check_position = tk.Button(button_frame, text="Sprawdź położenie UFO", command=check_position)
button_check_position.pack(side=tk.LEFT, padx=5)

button_calculate_distance = tk.Button(button_frame, text="Oblicz odległość UFO", command=calculate_distance)
button_calculate_distance.pack(side=tk.LEFT, padx=5)

button_randomize_ufo = tk.Button(button_frame, text="Przelosuj UFO", command=randomize_ufo)
button_randomize_ufo.pack(side=tk.LEFT, padx=5)

root.mainloop()
