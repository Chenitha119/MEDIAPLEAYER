from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.filechooser import FileChooserListView
from kivy.core.audio import SoundLoader

class MediaPlayerApp(App):
    def build(self):
        self.music_player = None  # Initialize the music player instance
        self.music_file = None
        self.playing = False

        layout = BoxLayout(orientation='vertical', spacing=10)
        
        self.play_button = Button(text='Play', size_hint=(None, None), size=(100, 50))
        self.play_button.bind(on_press=self.play)
        layout.add_widget(self.play_button)

        self.pause_button = Button(text='Pause', size_hint=(None, None), size=(100, 50))
        self.pause_button.bind(on_press=self.pause)
        layout.add_widget(self.pause_button)

        self.open_button = Button(text='Open', size_hint=(None, None), size=(100, 50))
        self.open_button.bind(on_press=self.open_file)
        layout.add_widget(self.open_button)

        self.volume_slider = Slider(min=0, max=1, value=0.5, size_hint=(None, None), width=200)
        self.volume_slider.bind(value=self.set_volume)
        layout.add_widget(self.volume_slider)

        self.file_chooser = FileChooserListView(path='.')
        layout.add_widget(self.file_chooser)

        return layout

    def play(self, instance):
        if self.music_file and not self.playing:
            self.music_player = SoundLoader.load(self.music_file)  # Load the selected audio file
            if self.music_player:
                self.music_player.play()
                self.playing = True

    def pause(self, instance):
        if self.playing and self.music_player:
            self.music_player.stop()
            self.playing = False

    def open_file(self, instance):
        self.music_file = self.file_chooser.selection and self.file_chooser.selection[0] or None

    def set_volume(self, instance, value):
        if self.playing and self.music_player:
            self.music_player.volume = float(value)

if __name__ == '__main__':
    MediaPlayerApp().run()
