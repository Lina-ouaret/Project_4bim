import neural_network_function as nn
import common_functions as cf
import numpy as np

if __name__ == "__main__" :

    # Upload photos
    from sklearn.datasets import fetch_olivetti_faces # Olivetti faces dataset
    dataset = fetch_olivetti_faces()
    X = dataset["data"]
    y = dataset["target"]

    # Split the dataset
    (X_train_, X_test_, y_train_, y_test_) = nn.split_dataset(X, y)

    # Creation model
    original_dim = X.shape[1]
    hidden_encoding_dim = 512
    encoding_dim = 64
    hidden_decoding_dim = 512
    dropout_level = 0.1
    (encoder_, decoder_, autoencoder_) = nn.model (original_dim,
                                                hidden_encoding_dim, encoding_dim,
                                                dropout_level, hidden_decoding_dim)

    # save model
    decoder_.save('decoder.h5')

    print('Decoder Saved!')

    # load model
    #savedDecoder=load_model('decoder.h5')
    #savedDecoder.summary()

    # Compile the model
    autoencoder_.compile(optimizer='adam', loss='binary_crossentropy')

    # Fit the model
    autoencoder_.fit(X_train_, X_train_,
                    epochs=300,
                    batch_size=64,
                    shuffle=True,
                    validation_data=(X_test_, X_test_))

    # Plot reconstruction
    encoded_imgs = encoder_.predict(X_test_)
    decoded_imgs = decoder_.predict(encoded_imgs)
    nn.save_reconstruction(9, decoded_imgs)

    # Plot the learning curve
    # history = autoencoder_.history.history
    # plt.plot(history['val_loss'],label="test")
    # plt.plot(history['loss'],label="training")
    # plt.xlabel("epochs")
    # plt.ylabel("Loss")
    # plt.legend()

    np.save('encoded_imgs.npy', encoded_imgs)
    #a2 = np.load('encoded_imgs.npy')
