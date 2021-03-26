#include <iostream>

using namespace std;
class Rectangle {
    protected:
        int width;
        int height;
        
    public: 
    void display() {
        
        cout << width << " " << height << endl;
        
    }
};

class RectangleArea : public Rectangle {
    public:
    void read_input(){
        cin >> width >> height;
    }
    
    void display() {
        cout << width*height << endl;
    }
};


int main()
{
    /*
     * Declare a RectangleArea object
     */
    RectangleArea r_area;
    
    /*
     * Read the width and height
     */
    r_area.read_input();
    
    /*
     * Print the width and height
     */
    r_area.Rectangle::display();
    
    /*
     * Print the area
     */
    r_area.display();
    
    return 0;
}

class Rectangle
{
public:
    Rectangle() = default;
    virtual void display() const { std::cout << _width << " " << _height << std::endl; }
    int area() const { return _width * _height; }
protected:
    int _width = 0;
    int _height = 0;
};

class RectangleArea : public Rectangle
{
public:
    RectangleArea() = default;
    virtual void display() const override { std::cout << area() << std::endl; }
    void read_input() { std::cin >> _width >> _height; }
};