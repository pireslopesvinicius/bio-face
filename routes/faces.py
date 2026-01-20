from services.faces import compare_faces
from fastapi import APIRouter, UploadFile, File, HTTPException, status, BackgroundTasks, Header, Request
from numpy import ndarray
from PIL import Image
from io import BytesIO
from models.schemas import FaceComparisonResult

router = APIRouter()


@router.post("/compare-faces")
async def compare_faces_endpoint(file1: UploadFile, file2: UploadFile, threshold: float = 0.3) -> FaceComparisonResult:
    if file1.content_type.split('/')[0] != 'image' or file2.content_type.split('/')[0] != 'image':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Both files must be images.")

    try:
        img1_bytes = await file1.read()
        img2_bytes = await file2.read()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error reading image files.")

    result = compare_faces(img1_bytes, img2_bytes, threshold)
    return result
