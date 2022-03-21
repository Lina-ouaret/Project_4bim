import neural_network_function as nn
import common_functions as cf
import numpy as np
import keras

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

    # save model
    np.save('encoded_imgs', encoded_imgs)
    np.save('decoded_imgs', decoded_imgs)
    decoder_.save('decoder.h5')



    # Plot the learning curve to test the model
    #loss_test(autoencoder_)

    #np.save('encoded_imgs.npy', encoded_imgs)
    #np.save('decoded_imgs.npy', decoded_imgs)

    #a2 = np.load('encoded_imgs.npy')
