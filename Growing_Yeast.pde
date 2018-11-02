Ring[] rings; // Declare the array

int maxnumRings = 5; 
int numRings = 1;
int currentRing = 0;

void setup() {
  size(1200, 1200);
  background(0);
}

void draw() {
}


void mousePressed() {
    numRings = 1;
    currentRing = 0;
    rings = new Ring[numRings]; // Create the array
    rings[currentRing] = new Ring(); // Create yeast object
    rings[currentRing].start(mouseX, mouseY);
    rings[currentRing].grow();  
    rings[currentRing].reproduce();
}

class Ring {
  float x, y;          // X-coordinate, y-coordinate
  float diameter;      // Diameter of the ring
  boolean on = false;  // Turns the display on and off
  boolean reproduce; //turns reproduction on or off
  float theta;  //budding parameter
  int quadrant; //budding parameter

  void start(float xpos, float ypos) {
    x = xpos;
    y = ypos; 
    diameter = 40;
    on = true;
    reproduce = false;
    quadrant = int(random(1,4));
  }  
  
  void grow() {
    print("grow1");
    while (on == true) {
      diameter += 0.5;
      if (diameter >= 40) {
        print("grow2");
        on = false;
        diameter = 40;
        reproduce = true;
      }
    }
    on = true;
  }
  
  void reproduce() {
    print("reproduce1");
    while (reproduce == true) {
      numRings += 1;
      currentRing += 1;
      rings = new Ring[numRings]; // Create the array
      rings[currentRing] = new Ring(); // Create yeast object
      //Budding parameters. These need to be played with so that the origin rotates with the angle of each new vector
      theta = random(HALF_PI); //angle of vector
      if (quadrant == 1){
        x = x+sin(theta)*40;
        y = y-cos(theta)*40;
      }
      if (quadrant == 2){
        x = x-sin(theta)*40;
        y = y-cos(theta)*40;
      }
      if (quadrant == 3){
        x = x-sin(theta)*40;
        y = y+cos(theta)*40;
      }
      if (quadrant == 4){
        x = x+sin(theta)*40+x;
        y = y+cos(theta)*40+y;
      }
      rings[currentRing].start((x), (y));
      rings[currentRing].grow();
      rings[currentRing].display();
      if (currentRing == maxnumRings) {
        reproduce = false;
      }
    }
  }
    
  void display() {
    print("display");
    if (on == true) {
      fill(200,100,0);
      strokeWeight(4);
      stroke(204, 153);
      ellipseMode(CENTER);
      ellipse(x, y, diameter, diameter);
    }
  }
}
