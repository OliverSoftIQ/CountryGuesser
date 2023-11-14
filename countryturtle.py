import pygame
import imageio

whole_world = ("CountryGuesser/images/World_map.gif")
brazil = ("CountryGuesser/images/brazil.gif")
test = "CountryGuesser/images/test.gif"

def display_gif(gif_path):
    # Initialize Pygame
    pygame.init()

    # Load the GIF using imageio
    gif = imageio.mimread(gif_path)

    # Set up the Pygame screen
    screen = pygame.display.set_mode(gif[0].shape[1::-1])

    # Set the Pygame window caption
    pygame.display.set_caption('Country Guesser')

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Run the Pygame event loop
    running = True
    frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display the current frame of the GIF
        frame_surface = pygame.surfarray.make_surface(gif[frame])
        screen.blit(frame_surface, (0, 0))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(10)  # Adjust the frames per second as needed

        # Increment the frame counter
        frame = (frame + 1) % len(gif)

    # Quit Pygame
    pygame.quit()

# Example usage
gif_path = "CountryGuesser/images/World_map.gif"
display_gif(gif_path)