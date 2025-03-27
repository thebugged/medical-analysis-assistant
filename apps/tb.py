# tb.py
import numpy as np
import tensorflow as tf
import streamlit as st
from PIL import Image

def tb_page():
    interpreter_tb = tf.lite.Interpreter(model_path='models/tb_model.tflite')
    interpreter_tb.allocate_tensors()
    input_details_tb = interpreter_tb.get_input_details()
    output_details_tb = interpreter_tb.get_output_details()
    
    # Display expected input shape for debugging
    expected_shape = input_details_tb[0]['shape']
    
    st.subheader("Tuberculosis Detection", divider='grey')
    st.caption("sample [image](https://www.kaggle.com/datasets/raddar/tuberculosis-chest-xrays-shenzhen)")
    
    # Show expected input shape (helpful for debugging)
    # st.text(f"Model expects input shape: {expected_shape}")
    
    uploaded_file = st.file_uploader("Upload a Chest X-ray Image", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=False)
        
        # Resize image to required dimensions
        image_array = np.asarray(image.resize((224, 224)))
        image_array = image_array.astype(np.float32) / 255.0
        
        # Handle different image formats (grayscale vs RGB)
        if len(image_array.shape) == 2:
            # Single channel (grayscale) - add channel dimension
            image_array = np.expand_dims(image_array, axis=-1)
            # If model expects 3 channels, convert grayscale to RGB
            if expected_shape[-1] == 3:
                image_array = np.repeat(image_array, 3, axis=-1)
        elif len(image_array.shape) == 3:
            # Check if image has the right number of channels
            if image_array.shape[2] != expected_shape[-1]:
                if image_array.shape[2] == 3 and expected_shape[-1] == 1:
                    # Convert RGB to grayscale if needed
                    image_array = np.mean(image_array, axis=-1, keepdims=True)
                elif image_array.shape[2] == 1 and expected_shape[-1] == 3:
                    # Convert grayscale to RGB if needed
                    image_array = np.repeat(image_array, 3, axis=-1)
        
        # Add batch dimension
        image_array = np.expand_dims(image_array, axis=0)
        
        # Show actual input shape (for debugging)
        # st.text(f"Processed image shape: {image_array.shape}")
        
        try:
            # Set the tensor and run inference
            interpreter_tb.set_tensor(input_details_tb[0]['index'], image_array)
            interpreter_tb.invoke()
            predictions = interpreter_tb.get_tensor(output_details_tb[0]['index'])
            
            # Process the results
            class_index = np.argmax(predictions)
            if class_index == 1:
                st.success("Tuberculosis Detected!")
            else:
                st.success("No Tuberculosis Detected.")
                
            # Show prediction probabilities
            st.text(f"Prediction confidence: {predictions[0][class_index]:.2f}")
            
        except Exception as e:
            st.error(f"Error during prediction: {e}")

if __name__ == "__main__":
    tb_page()
