# Pokopia-Info-CDN

Pokopia-Info-CDN은 [pokopia-info.vercel.app](https://pokopia-info.vercel.app) 서비스를 위한 포코피아(Pokopia) 관련 에셋(배지, 아이템, 포켓몬 등)을 저장하고 제공하는 이미지 CDN 리포지토리입니다.

## 기능

*   **이미지 에셋 저장소**: `badges`, `items`, `pokemon`, `habitats`, `specialties`, `types` 등의 디렉토리로 구조화되어 다양한 이미지 에셋을 관리합니다.
*   **WebP 자동 변환**: 포함된 Node.js 스크립트(`optimize-images.js`)를 통해 원본 이미지(`png`, `jpg`, `jpeg`)를 무손실 WebP 형식으로 자동 최적화하고 ⚠️ **원본 파일을 삭제**하여 저장 용량을 최소화합니다.
*   **CDN 캐시 자동 초기화**: `main` 브랜치에 수정된 `.webp` 파일이 푸시되면 GitHub Actions(`.github/workflows/purge-cdn.yml`)가 자동으로 트리거되어 jsDelivr CDN 캐시를 초기화합니다. 이는 봇에 의한 커밋도 포함하여 적용됩니다.

## 스크립트 사용법

리포지토리에 `package.json` 파일이 포함되어 있지 않으므로, 이미지 최적화 스크립트를 실행하려면 로컬 환경에 **Node.js**가 설치되어 있어야 하며 의존성 패키지를 직접 설치해야 합니다.

1.  필요한 의존성 패키지 설치:
    ```bash
    npm install sharp glob
    ```
2.  새로운 이미지를 관련 폴더(예: `pokemon/`, `items/`)에 추가합니다.
3.  최적화 스크립트 실행:
    ```bash
    node optimize-images.js
    ```
    🚨 **주의**: 이 스크립트를 실행하면 추가된 `png`, `jpg`, `jpeg` 파일들이 WebP로 변환되고 **원본 파일은 즉시 삭제**됩니다! 필요한 원본 파일은 미리 백업해 두세요.

## CDN URL 사용 예시

jsDelivr를 통해 에셋에 접근할 수 있습니다.

*   **기본 URL (Base URL)**: `https://cdn.jsdelivr.net/gh/FOJF/Pokopia-Info-CDN@main/`
*   **사용 예시**: `https://cdn.jsdelivr.net/gh/FOJF/Pokopia-Info-CDN@main/pokemon/pikachu.webp`
