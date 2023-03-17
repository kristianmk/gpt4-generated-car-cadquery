import cadquery as cq


def create_car_model(length, width, height, wheel_radius, wheel_width):
    # Car body
    main_body = (
        cq.Workplane("XY")
        .rect(length * 0.9, width * 0.9)
        .extrude(height * 0.4)
    )

    roof = (
        cq.Workplane("XY")
        .transformed(offset=(0, 0, height * 0.4))
        .ellipse(length * 0.45, width * 0.45)
        .extrude(height * 0.3)
    )

    body = main_body.union(roof)

    # Wheel
    wheel = (
        cq.Workplane("XZ")
        .circle(wheel_radius)
        .extrude(wheel_width)
    )

    # Wheel positions
    wheel_positions = [
        (-length * 0.35, -width * 0.5 - wheel_width / 2, height * 0.1),
        (-length * 0.35, width * 0.5 + wheel_width / 2, height * 0.1),
        (length * 0.35, -width * 0.5 - wheel_width / 2, height * 0.1),
        (length * 0.35, width * 0.5 + wheel_width / 2, height * 0.1),
    ]

    for pos in wheel_positions:
        body = body.union(wheel.translate(pos))

    return body


# Parameters for the car model
length = 70
width = 30
height = 20
wheel_radius = 8
wheel_width = 6

# Create the 3D car model
car_model = create_car_model(length, width, height, wheel_radius, wheel_width)

# Export the model to a STEP file
car_model.val().exportStep("detailed_car_model.step")
