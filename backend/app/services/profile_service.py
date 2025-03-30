from sqlalchemy import select
from sqlalchemy.orm import Session
from .. models import UserProfile
from .. utils.logging import info, error
from .. services.user_service import UserService
from hashlib import sha256

class ProfileService:

    @staticmethod
    def sanitizer(value: str, type: str) -> bool:
        """Sanitize the input value based on the type."""
        pass

    @staticmethod
    def safe_get_profile(session: Session, user_id: int) -> UserProfile | None:
        profile = session.execute(
            select(UserProfile)
            .filter(UserProfile.user_id == user_id)
            .with_for_update()
        ).scalar_one_or_none()
        if not profile:
            error(f"Profile for user {user_id} not found.", __name__)
            return None
        return profile
    
    @staticmethod
    def safe_create_profile(session: Session, user_id: int, profile: dict) -> bool:
        for attr in ['profile_name', 'full_name', 'bio', 'country', 'city', 'birthdate']:
            if attr not in profile:
                error(f"Missing {attr} in profile creation.", __name__)
                return False

        username = UserService.safe_get_user(session, user_id).username
        address = sha256(username.encode()).hexdigest()
        
        try:
            new_profile = UserProfile(
                user_id=user_id,
                username=username,
                profile_name=profile['profile_name'],
                full_name=profile['full_name'],
                bio=profile['bio'] if 'bio' in profile else '',
                location=profile['city'] + ', ' + profile['country'],
                birthdate=profile['birthdate'],
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
        