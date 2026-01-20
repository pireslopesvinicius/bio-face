from deepface import DeepFace
from PIL import Image
import numpy as np
from io import BytesIO
from models.schemas import FaceComparisonResult


def compare_faces(img1: bytes, img2: bytes, threshold: float = 0.3) -> FaceComparisonResult:
    # Converte bytes para numpy array
    img1_array = np.array(Image.open(BytesIO(img1)))
    img2_array = np.array(Image.open(BytesIO(img2)))
    
    result = DeepFace.verify(img1_array, img2_array, model_name='ArcFace', threshold=threshold)
    
    return FaceComparisonResult(
        verified=result['verified'],
        distance=result['distance'],
        threshold=threshold,
        confidence=result.get('confidence', 0.0),
        model='ArcFace'
    )
