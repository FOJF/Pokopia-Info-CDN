const sharp = require('sharp');
const glob = require('glob');
const path = require('path');

// 설정
const CONCURRENCY = 8; // CPU 사양에 따라 조절 (8개 파일 동시 처리)

async function optimizeToLosslessWebp() {
  console.log('🔍 이미지 검색 중...');
  const files = glob.sync('**/*.{png,jpg,jpeg}', {
    ignore: ['node_modules/**', 'test_lossless/**', 'dist/**', '**/*.webp'],
    nodir: true
  });

  console.log(`🚀 총 ${files.length}개의 파일을 무손실 WebP로 변환합니다.`);
  console.log('💡 품질은 100% 유지되며, 원본 파일은 수정되지 않습니다.');

  let processedCount = 0;
  let skipCount = 0;
  const startTime = Date.now();

  for (let i = 0; i < files.length; i += CONCURRENCY) {
    const chunk = files.slice(i, i + CONCURRENCY);
    await Promise.all(chunk.map(async (file) => {
      try {
        const ext = path.extname(file).toLowerCase();
        const dir = path.dirname(file);
        const name = path.basename(file, ext);
        const webpPath = path.join(dir, `${name}.webp`);

        // 이미 동일한 이름의 webp 파일이 있는지 확인 (선택 사항)
        // if (fs.existsSync(webpPath)) { skipCount++; return; }

        await sharp(file)
          .webp({ lossless: true, effort: 6 }) // 무손실 압축, 최대 효율
          .toFile(webpPath);

        processedCount++;
        if (processedCount % 100 === 0) {
          console.log(`✅ 진행률: ${processedCount}/${files.length} (${Math.round(processedCount / files.length * 100)}%)`);
        }
      } catch (err) {
        console.error(`❌ 에러 발생 (${file}):`, err.message);
      }
    }));
  }

  const duration = (Date.now() - startTime) / 1000;
  console.log(`\n🎉 모든 작업 완료!`);
  console.log(`📊 처리된 파일: ${processedCount}개`);
  console.log(`⏱️ 소요 시간: ${duration.toFixed(2)}초`);
}

optimizeToLosslessWebp();
