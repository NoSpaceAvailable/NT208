from sqlalchemy import select
from sqlalchemy.orm import Session
from .. models import UserProfile
from .. utils.logging import info, error
from .. services.user_service import UserService
from hashlib import sha256

class ProfileService:

    @staticmethod
    def sanitizer(profile: dict) -> bool:
        """Sanitize the input value"""
        if not isinstance(profile, dict):
            error("Profile must be a dictionary", __name__)
            return False

        required_fields = ['profile_name', 'full_name', 'bio', 'country', 'city', 'birthdate']
        for field in required_fields:
            if field not in profile:
                error(f"Missing required field: {field}", __name__)
                return False
            if not isinstance(profile[field], str):
                error(f"Field {field} must be a string", __name__)
                return False
            profile[field] = profile[field].strip()

        if profile['profile_name'] == '':
            error("Profile name cannot be empty", __name__)
            return False

        if len(profile['profile_name']) > 50:
            error("Profile name too long (max 50 characters)", __name__)
            return False

        if len(profile['full_name']) > 100:
            error("Full name too long (max 100 characters)", __name__)
            return False

        if len(profile['bio']) > 500:
            error("Bio too long (max 500 characters)", __name__)
            return False

        if len(profile['country']) > 50:
            error("Country name too long (max 50 characters)", __name__)
            return False

        if len(profile['city']) > 50:
            error("City name too long (max 50 characters)", __name__)
            return False

        # Basic date format validation (YYYY-MM-DD)
        date_parts = profile['birthdate'].split('-')
        if len(date_parts) != 3:
            error("Invalid date format. Use YYYY-MM-DD", __name__)
            return False

        try:
            year, month, day = map(int, date_parts)
            if not (1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31):
                error("Invalid date values", __name__)
                return False
        except ValueError:
            error("Invalid date format", __name__)
            return False
        return True

    @staticmethod
    def safe_get_profile(session: Session, user_id: int) -> UserProfile | None:
        try:
            profile = session.execute(
                select(UserProfile)
                .filter(UserProfile.user_id == user_id)
            ).scalar_one_or_none()
            if not profile:
                error(f"Profile for user {user_id} not found.", __name__)
            return profile
        except Exception as e:
            error(f"Error while fetching profile: {e}")
            session.rollback()
            return None
    
    @staticmethod
    def safe_create_profile(session: Session, user_id: int, profile: dict) -> bool:
        for attr in ['profile_name', 'full_name', 'bio', 'country', 'city', 'birthdate']:
            if attr not in profile:
                error(f"Missing {attr} in profile creation.", __name__)
                return False

        username = UserService.safe_get_user(session, user_id).username
        address = sha256(username.encode()).hexdigest()
        
        try:
            if not ProfileService.sanitizer(profile):
                raise ValueError("Invalid profile")
            
            new_profile = UserProfile(
                user_id=user_id,
                username=username,
                profile_name=profile['profile_name'].strip(),
                full_name=profile['full_name'].strip(),
                bio=profile['bio'].strip() if 'bio' in profile else '',
                location=profile['city'].strip() + ', ' + profile['country'].strip(),
                birthdate=profile['birthdate'].strip(),
                wallet_address=address
            )
            session.add(new_profile)
            session.commit()
            info(f"Profile created for user {user_id}.", __name__)
            return True
        except Exception as e:
            error(f"Failed to create profile for {user_id}, reason: {str(e)}", __name__)
            session.rollback()
            return False
    
    @staticmethod
    def safe_update_profile(session: Session, user_id: int, new_profile: dict) -> bool:
        profile = ProfileService.safe_get_profile(session, user_id)
        if not profile:
            return False
        try:
            profile.profile_name = new_profile.get('username', profile.username)
            profile.full_name = new_profile.get('full_name', profile.full_name)
            profile.bio = new_profile.get('bio', profile.bio)
            profile.location = new_profile.get('location', profile.location)
            profile.birthdate = new_profile.get('birthdate', profile.birthdate) 

            session.commit()
            info(f"Profile updated for user {user_id}.", __name__)
            return True
        except Exception as e:
            error(f"Failed to update profile for {user_id}, reason: {str(e)}", __name__)
            session.rollback()
            return False
        
    @staticmethod
    def get_profile_for_display(session: Session, user_id: int) -> dict | None:
        profile = ProfileService.safe_get_profile(session, user_id)
        if not profile:
            return None
        return {
            'profile_name': profile.profile_name,
            'full_name': profile.full_name,
            'bio': profile.bio,
            'location': profile.location,
            'birthdate': profile.birthdate,
            'joined_at': profile.joined_at,
            'wallet_address': profile.wallet_address
        }
        