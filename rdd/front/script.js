// Обработка загрузки файла
document.getElementById('uploadBtn').addEventListener('click', function() {
    document.getElementById('fileInput').click();
});

document.getElementById('fileInput').addEventListener('change', function(e) {
    if (e.target.files.length > 0) {
        const file = e.target.files[0];
        processImage(file);
    }
});

// Обработка drag and drop
const dropZone = document.getElementById('dropZone');

dropZone.addEventListener('dragover', function(e) {
    e.preventDefault();
    this.classList.add('border-primary');
    this.style.backgroundColor = '#e8f0fe';
});

dropZone.addEventListener('dragleave', function(e) {
    e.preventDefault();
    this.classList.remove('border-primary');
    this.style.backgroundColor = '';
});

dropZone.addEventListener('drop', function(e) {
    e.preventDefault();
    this.classList.remove('border-primary');
    this.style.backgroundColor = '';
    
    if (e.dataTransfer.files.length > 0) {
        const file = e.dataTransfer.files[0];
        processImage(file);
    }
});

// Определение местоположения
document.getElementById('locationBtn').addEventListener('click', function() {
    if (navigator.geolocation) {
        this.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Определение...';
        this.disabled = true;
        
        navigator.geolocation.getCurrentPosition(
            function(position) {
                determineCity(position.coords.latitude, position.coords.longitude);
            },
            function(error) {
                document.getElementById('locationBtn').innerHTML = '<i class="fas fa-map-marker-alt me-2"></i>Определить город';
                document.getElementById('locationBtn').disabled = false;
                alert('Не удалось определить местоположение: ' + error.message);
            }
        );
    } else {
        alert('Геолокация не поддерживается вашим браузером');
    }
});

// Функция для определения города по координатам
function determineCity(lat, lng) {
    setTimeout(function() {
        const cities = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Тюмень'];
        const randomCity = cities[Math.floor(Math.random() * cities.length)];
        
        document.getElementById('cityName').textContent = randomCity;
        document.getElementById('locationInfo').style.display = 'block';
        
        document.getElementById('locationBtn').innerHTML = '<i class="fas fa-map-marker-alt me-2"></i>Определить город';
        document.getElementById('locationBtn').disabled = false;
    }, 1500);
}

// Функция для обработки изображения
function processImage(file) {
    const dropZone = document.getElementById('dropZone');
    const resultsPanel = document.getElementById('resultsPanel');
    const originalImage = document.getElementById('originalImage');
    const resultAlert = document.getElementById('resultAlert');

    
    const reader = new FileReader();
    reader.onload = function(e) {
        originalImage.src = e.target.result;
    };
    reader.readAsDataURL(file);
    
    
    
    
    dropZone.style.display = 'none';
    resultsPanel.style.display = 'block';
    resultAlert.className = 'alert alert-info';
    resultAlert.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i><strong>Анализ в процессе...</strong> Пожалуйста, подождите.';
    
    document.getElementById('aiResultsPlaceholder').innerHTML = '';
    document.getElementById('defectList').innerHTML = '';
    document.getElementById('reportBtn').disabled = true;
   
    setTimeout(function() {
        callAIAnalysis(file);
    }, 2000);
}

function callAIAnalysis(file)
{
    var fName = file.name;
    console.log(fName)
}

// Кнопка "Попробовать еще раз"
document.getElementById('tryAgainBtn').addEventListener('click', function() {
    document.getElementById('fileInput').value = '';
    document.getElementById('dropZone').style.display = 'block';
    document.getElementById('resultsPanel').style.display = 'none';
});

// Кнопка отправки в дорожную службу
document.getElementById('reportBtn').addEventListener('click', function() {
    alert('Функция отправки в дорожную службу будет реализована после подключения ИИ');
});