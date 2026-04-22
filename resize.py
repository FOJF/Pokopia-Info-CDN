import os
import sys
from PIL import Image
from pathlib import Path

def resize_images(source_dir, target_dir, width, height):
    """
    지정한 소스 폴더의 이미지를 리사이징하여 대상 폴더에 저장합니다. (원본 유지)
    """
    if not os.path.exists(source_dir):
        print(f"❌ 에러: 소스 폴더 '{source_dir}'가 존재하지 않습니다.")
        return

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"📁 대상 폴더 '{target_dir}'를 생성했습니다.")

    # 지원하는 이미지 확장자
    extensions = ['*.webp', '*.png', '*.jpg', '*.jpeg']
    files = []
    for ext in extensions:
        files.extend(list(Path(source_dir).glob(ext)))
    
    if not files:
        print(f"❓ '{source_dir}' 폴더에 처리할 이미지가 없습니다.")
        return

    print(f"🚀 총 {len(files)}개의 이미지를 {width}x{height} 크기로 리사이징합니다.")
    print(f"📂 경로: {source_dir} -> {target_dir}")

    processed_count = 0
    for i, file_path in enumerate(files):
        try:
            with Image.open(file_path) as img:
                # 비율 유지하며 리사이징 (썸네일 방식)
                img.thumbnail((width, height), Image.Resampling.LANCZOS)
                
                target_path = Path(target_dir) / file_path.name
                # 원본 포맷 유지하며 저장
                img.save(target_path)
                
            processed_count += 1
            if processed_count % 100 == 0:
                print(f"✅ 진행률: {processed_count}/{len(files)}")
        except Exception as e:
            print(f"❌ 에러 발생 ({file_path.name}): {e}")

    print(f"\n🎉 모든 작업 완료! (총 {processed_count}개 처리)")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("📖 사용법: python3 resize.py [소스폴더] [대상폴더] [가로(선택)] [세로(선택)]")
        print("💡 예시: python3 resize.py pokemon_copy pokemon 160 160")
        sys.exit(1)

    src = sys.argv[1]
    dest = sys.argv[2]
    w = int(sys.argv[3]) if len(sys.argv) > 3 else 160
    h = int(sys.argv[4]) if len(sys.argv) > 4 else w  # 세로 미지정 시 가로와 동일하게 설정

    resize_images(src, dest, w, h)
