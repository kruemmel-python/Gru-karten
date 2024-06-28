# main.py
# This file is part of the proprietary part of the Greeting Card Generator.

import sys
import random
import math
from PySide6.QtWidgets import QApplication, QColorDialog, QMessageBox
from PySide6.QtGui import QColor, QImage, QPainter, QPen, QFont, QPolygonF, QPixmap
from PySide6.QtCore import Qt, QPointF
from gui_component import GreetingCardApp, PreviewDialog
import gui_component

class GreetingCardGenerator:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ex = GreetingCardApp()
        self.bg_color = QColor(255, 255, 255)
        self.font_color = QColor(0, 0, 0)
        self.frame_color = QColor(0, 0, 0)
        
        # Connect signals from the GUI to the proprietary methods
        self.ex.connect_signals(self.choose_color, self.choose_font_color, self.choose_frame_color, self.preview_greeting_card, self.create_greeting_card)
    
    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.bg_color = color
    
    def choose_font_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.font_color = color

    def choose_frame_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.frame_color = color
    
    def preview_greeting_card(self):
        text = self.ex.text_entry.toPlainText()
        design = self.ex.design_combo.currentText()
        apply_both = self.ex.combine_checkbox.isChecked()
        
        if not text and design == "Text-based":
            QMessageBox.critical(self.ex, "Error", "Please enter greeting text.")
            return
        
        image = self.generate_card(text, design, apply_both)
        self.show_preview(image)
    
    def create_greeting_card(self):
        text = self.ex.text_entry.toPlainText()
        design = self.ex.design_combo.currentText()
        apply_both = self.ex.combine_checkbox.isChecked()
        
        if not text and design == "Text-based":
            QMessageBox.critical(self.ex, "Error", "Please enter greeting text.")
            return
        
        image = self.generate_card(text, design, apply_both)
        image.save(f'greeting_card_{design}.png')
        QMessageBox.information(self.ex, "Success", "Greeting card created successfully.")
    
    def generate_card(self, text, design, apply_both):
        card_width, card_height = 800, 600
        image = QImage(card_width, card_height, QImage.Format_RGB32)
        image.fill(self.bg_color)
        
        painter = QPainter(image)
        
        if design == "Text-based" or (apply_both and design == "Stars and Clouds"):
            self.generate_text_based(painter, card_width, card_height, text)
        
        if design == "Frame" or (apply_both and design == "Stars and Clouds"):
            frame_type = self.ex.frame_combo.currentText()
            add_shadow = self.ex.shadow_checkbox.isChecked()
            self.generate_frame(painter, card_width, card_height, frame_type, add_shadow)
        
        if design == "Stars and Clouds" or (apply_both and design == "Stars and Clouds"):
            self.generate_stars_and_clouds(painter, card_width, card_height)

        self.draw_text(painter, card_width, card_height, text)
        
        painter.end()
        return image
    
    def show_preview(self, image):
        dialog = PreviewDialog(image, self.ex)
        dialog.exec()
    
    def generate_text_based(self, painter, width, height, text):
        # Placeholder for additional logic for text-based design
        pass
    
    def generate_stars_and_clouds(self, painter, width, height):
        for _ in range(20):
            x, y = random.randint(0, width), random.randint(0, height)
            size = random.randint(20, 50)
            self.draw_star(painter, x, y, size, QColor(random.choice(["yellow", "white"])))
        
        for _ in range(5):
            x, y = random.randint(0, width), random.randint(0, height)
            size = random.randint(50, 100)
            self.draw_cloud(painter, x, y, size, QColor("lightgrey"))

    def draw_star(self, painter, x, y, size, color):
        painter.setPen(QPen(color, 2))
        painter.setBrush(color)
        points = []
        for i in range(5):
            angle = i * 144 * (math.pi / 180)
            x_star = x + size * math.cos(angle)
            y_star = y - size * math.sin(angle)
            points.append(QPointF(x_star, y_star))
        painter.drawPolygon(QPolygonF(points))

    def draw_cloud(self, painter, x, y, size, color):
        painter.setPen(QPen(color, 2))
        painter.setBrush(color)
        for i in range(5):
            x_offset = random.randint(-size // 2, size // 2)
            y_offset = random.randint(-size // 4, size // 4)
            radius = size // random.randint(3, 6)
            painter.drawEllipse(x + x_offset, y + y_offset, radius, radius)

    def generate_frame(self, painter, width, height, frame_type, add_shadow):
        color = self.frame_color
        if add_shadow:
            shadow_color = QColor(0, 0, 0, 128)
            shadow_offset = 5
            painter.setPen(QPen(shadow_color, 3))
            self.draw_frame(painter, width, height, frame_type, shadow_offset)
        
        painter.setPen(QPen(color, 3))
        self.draw_frame(painter, width, height, frame_type)

    def draw_frame(self, painter, width, height, frame_type, offset=0):
        step = 20
        if frame_type == "Straight":
            self.draw_straight_frame(painter, width, height, step, offset)
        elif frame_type == "Zigzag":
            self.draw_zigzag_frame(painter, width, height, step, offset)
        elif frame_type == "Wavy":
            self.draw_wavy_frame(painter, width, height, step, offset)
        elif frame_type == "Looped":
            self.draw_looped_frame(painter, width, height, step, offset)

    def draw_straight_frame(self, painter, width, height, step, offset):
        painter.drawRect(offset, offset, width - 2 * offset, height - 2 * offset)

    def draw_zigzag_frame(self, painter, width, height, step, offset):
        for x in range(0, width, step):
            painter.drawLine(x + offset, offset, x + step // 2 + offset, step + offset)
            painter.drawLine(x + step // 2 + offset, step + offset, x + step + offset, offset)
        for x in range(0, width, step):
            painter.drawLine(x + offset, height + offset, x + step // 2 + offset, height - step + offset)
            painter.drawLine(x + step // 2 + offset, height - step + offset, x + step + offset, height + offset)
        for y in range(0, height, step):
            painter.drawLine(offset, y + offset, step + offset, y + step // 2 + offset)
            painter.drawLine(step + offset, y + step // 2 + offset, offset, y + step + offset)
        for y in range(0, height, step):
            painter.drawLine(width + offset, y + offset, width - step + offset, y + step // 2 + offset)
            painter.drawLine(width - step + offset, y + step // 2 + offset, width + offset, y + step + offset)

    def draw_wavy_frame(self, painter, width, height, step, offset):
        for x in range(0, width, step):
            y = int(10 * math.sin((x + offset) * 0.1) + 20)
            painter.drawLine(x + offset, y + offset, x + step + offset, int(10 * math.sin((x + step + offset) * 0.1) + 20) + offset)
            painter.drawLine(x + offset, height - y + offset, x + step + offset, height - int(10 * math.sin((x + step + offset) * 0.1) + 20) + offset)
        for y in range(0, height, step):
            x = int(10 * math.sin((y + offset) * 0.1) + 20)
            painter.drawLine(x + offset, y + offset, int(10 * math.sin((y + step + offset) * 0.1) + 20) + offset, y + step + offset)
            painter.drawLine(width - x + offset, y + offset, width - int(10 * math.sin((y + step + offset) * 0.1) + 20) + offset, y + step + offset)

    def draw_looped_frame(self, painter, width, height, step, offset):
        for x in range(0, width, step):
            painter.drawArc(x + offset, offset, step, step, 0, 180 * 16)
            painter.drawArc(x + offset, height - step + offset, step, step, 180 * 16, 360 * 16)
        for y in range(0, height, step):
            painter.drawArc(offset, y + offset, step, step, 90 * 16, 270 * 16)
            painter.drawArc(width - step + offset, y + offset, step, step, 270 * 16, 450 * 16)

    def draw_text(self, painter, width, height, text):
        font = QFont(self.ex.font_combo.currentFont().family(), self.ex.font_size_spinbox.value())
        painter.setFont(font)
        
        alignment = self.ex.align_combo.currentText()
        if alignment == "Left":
            align = Qt.AlignLeft
        elif alignment == "Center":
            align = Qt.AlignCenter
        elif alignment == "Right":
            align = Qt.AlignRight
        elif alignment == "Justify":
            align = Qt.AlignJustify
        
        text_rect = painter.boundingRect(0, 0, width, height, align | Qt.TextWordWrap, text)
        painter.setPen(QPen(self.font_color))
        painter.drawText(text_rect, align | Qt.TextWordWrap, text)

if __name__ == '__main__':
    generator = GreetingCardGenerator()
    generator.ex.show()
    sys.exit(generator.app.exec())
