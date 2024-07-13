// Create the scene, camera, and renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(8, window.innerWidth/2 / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({alpha : true});
renderer.setSize(500, 500);
renderer.setClearColor(0x404040, 0);
document.getElementById('container').appendChild(renderer.domElement);

// Set up OrbitControls
const controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.25;
controls.enableZoom = true;

// Load the GLTF model
const loader = new THREE.GLTFLoader();
loader.load('/static/scene.gltf', function (gltf) {
    gltf.scene.position.set(0, -0.1, 0);
    scene.add(gltf.scene);
}, undefined, function (error) {
    console.error(error);
});

// Position the camera
camera.position.set(-1.5, 0.5, 3);

// Lighting
const ambientLight = new THREE.AmbientLight(0x404040); // Soft white light
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(1, 1, 2).normalize();
directionalLight.castShadow = true;
scene.add(directionalLight);

const pointLight = new THREE.PointLight(0xffffff, 1, 100);
pointLight.position.set(0, 1, 3); // Position the point light
directionalLight.castShadow = true;
scene.add(pointLight);

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    controls.update(); // Only required if controls.enableDamping = true, or if controls.autoRotate = true
    renderer.render(scene, camera);
}

animate();

// Handle window resize
window.addEventListener('resize', function() {
    const width = window.innerWidth/3;
    const height = 500;
    renderer.setSize(width, height);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
});

scene.background = null;