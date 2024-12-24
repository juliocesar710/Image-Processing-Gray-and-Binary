def save_image(image, output_path):
    cv2.imwrite(output_path, image)

def show_image(image, title):
    plt.imshow(image, cmap="gray")
    plt.title(title)
    plt.axis('off')
    plt.show()
